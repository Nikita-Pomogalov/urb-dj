from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def func(request):
    return render(request, 'second_task/func_template.html')

def cls(request):
    return render(request, 'second_task/class_template.html')