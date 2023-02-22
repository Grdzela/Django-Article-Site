from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html',)


def about(request):
    return render(request, 'main/about.html')


def layout(request):
    return render(request, 'main/layout.html')
