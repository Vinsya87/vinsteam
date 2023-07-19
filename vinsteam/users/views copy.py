from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

User = get_user_model()


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse(
                {'success': False, 'message': 'Неверный логин или пароль.'})
    else:
        csrf_token = get_token(request)
        return render(request, 'users/login.html', {'csrf_token': csrf_token})


from django.contrib.auth import authenticate, login
from django.http import JsonResponse


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']
        if password != password_repeat:
            return JsonResponse({'success': False, 'message': 'Пароли не совпадают'})
        try:
            # Проверяем, существует ли пользователь с таким именем
            if User.objects.filter(username=username).exists():
                return JsonResponse({'success': False, 'message': 'Пользователь с таким именем уже существует.'})

            # Проверяем, существует ли пользователь с такой почтой
            if User.objects.filter(email=email).exists():
                return JsonResponse({'success': False, 'message': 'Пользователь с такой почтой уже существует.'})

            # Создаем нового пользователя
            user = User.objects.create_user(username=username, email=email, password=password)
            # Аутентификация пользователя
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'message': 'Ошибка при аутентификации пользователя.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': 'Ошибка при создании пользователя. Попробуйте еще раз позже. Ошибка: {}'.format(str(e))})
    else:
        return JsonResponse({'success': False, 'message': 'Метод запроса должен быть POST.'})





@method_decorator(login_required, name='dispatch')
class CustomLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': ['Logout error']})