from articles.mixins import MenuView
from config_site.models import Config
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET
from django.views.generic import ListView
from django.views.generic.edit import FormView
from mail_post.views import FeedView
from reviews.forms import ReviewForm
from reviews.mixins import ReviewMixin
from reviews.models import Review

from .models import Review


class AddReviewView(ReviewMixin, FormView):
    success_url = ''
    form_class = ReviewForm

    def form_valid(self, form):
        if self.request.POST.get('privacy_policy') != 'on':
            return JsonResponse({'success': False, 'errors': {'privacy_policy': ['Подтвердите согласие с политикой безопасности']}}, status=400)
        review = form.save(commit=False)
        review.user = self.request.user
        review.save()
        data = {'success': True}
        # Отправляем уведомление на email из модели Config
        config = Config.objects.first()
        recipient_list = [config.email]
        if recipient_list:
            subject = 'Новый отзыв добавлен'
            username = self.request.POST.get('username', '')
            message = f'Новый отзыв был добавлен на сайте пользователем {username}.'
            email_from = f'Cайт - <{settings.EMAIL_HOST_USER}>'
            send_mail(
                subject, message,
                email_from, recipient_list,
                fail_silently=False)
        return JsonResponse(data)

    def form_invalid(self, form):
        data = {'success': False, 'errors': form.errors}
        return JsonResponse(data, status=400)


@require_GET
def get_full_review(request):
    review_id = request.GET.get('review_id')
    review = get_object_or_404(Review, id=review_id)
    data = {
        'created_at': review.created_at.strftime('%d.%m.%Y'),
        'name': review.name,
        'text': review.text
    }
    return JsonResponse({'review': data})


class ReviewsList(
        MenuView,
        FeedView,
        ReviewMixin,
        ListView):
    model = Review
    context_object_name = 'posts'
    template_name = 'reviews/review_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_enabled=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meta_title'] = 'Отзывы о нашей стоматолгии'
        context['meta_description'] = 'Ознакомьтесь с отзывами о стоматологии в Томске. Узнайте, что говорят пациенты о наших услугах. Качественное лечение, профессиональные врачи. Оставьте свой отзыв!'
        return context
