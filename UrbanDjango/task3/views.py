from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def func(request):
    return render(request, 'third_task/platform.html')

