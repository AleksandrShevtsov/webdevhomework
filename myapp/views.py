from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, World!")


def hello(request):
    return HttpResponse("Hello, your_name")


def chao(request):
    return HttpResponse("Chao, your_name")

# Create your views here.
