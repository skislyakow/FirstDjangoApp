from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Привет мир. Мы на главной приложения POLLS")


# Create your views here.
