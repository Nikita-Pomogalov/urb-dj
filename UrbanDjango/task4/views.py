from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def func(request):
    sp = ['Главная', 'Магазин', 'Корзина']
    context = {
        'sp': sp,
    }
    return render(request, 'platform.html', context)

def games(request):
    games = ['Atomic Heart', 'Cyperpunk 2077', 'PayDay 2']
    context = {
        'games': games
    }
    return render(request, 'games.html', context)