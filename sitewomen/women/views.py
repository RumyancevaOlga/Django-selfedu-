from django.http import HttpResponse
from django.shortcuts import render


# самая простая функция представления
def index(request): # HttpRequest
    return  HttpResponse("Страница приложения women.")

def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")
