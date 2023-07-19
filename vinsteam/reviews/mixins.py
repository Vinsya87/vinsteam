from django.shortcuts import redirect
from django.views.generic.edit import FormMixin
from reviews.forms import ReviewForm
from reviews.models import Review


class ReviewMixin(FormMixin):
    form_class = ReviewForm

    def form_valid(self, form):
        form.save()
        return redirect(self.request.path)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = self.form_class()
        return context

    def get_enabled_reviews(self):
        return Review.objects.filter(is_enabled=True)
