from audioop import error

from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse


# Create your views here.

def sign_up_by_html(request):
    users = ['Sasha', 'Petr', 'Maksim']
    info = {
        'error': '',
    }
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        r_pass = request.POST.get('r_pass')
        age = request.POST.get('age')
        if password == r_pass and int(age) > 18 and login not in users:
            return HttpResponse(f'Приветствуем, {login}')
        if password != r_pass:
            fail = 'Пароли не совпадают'
            info = {
                'error': fail,
            }
        if int(age) < 18:
            fail = 'Вы должны быть старше 18'
            info = {
                'error': fail,
            }
        if login in users:
            fail = 'Пользователь уже существует'
            info = {
                'error': fail,
            }

    return render(request, 'fifth_task/registration_page.html', context=info)

def sign_up_by_django(request):
    users = ['Sasha', 'Petr', 'Maksim']
    info = {
        'error': '',
    }
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            r_pass = form.cleaned_data['r_pass']
            age = form.cleaned_data['age']
            if password == r_pass and int(age) > 18 and login not in users:
                return HttpResponse(f'Приветствуем, {login}')
            if password != r_pass:
                fail = 'Пароли не совпадают'
                info = {
                    'error': fail,
                }
                return render(request, 'fifth_task/registration_page.html', context=info)
            if int(age) < 18:
                fail = 'Вы должны быть старше 18'
                info = {
                    'error': fail,
                }
                return render(request, 'fifth_task/registration_page.html', context=info)
            if login in users:
                fail = 'Пользователь уже существует'
                info = {
                    'error': fail,
                }
            return render(request, 'fifth_task/registration_page.html', context=info)
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', {'form': form})