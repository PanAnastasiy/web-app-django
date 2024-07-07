from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Проверка работы<h1>")


def about(request):
    return HttpResponse("<h1>О мне любимому<h1>")


def genshin(request):
    return HttpResponse('<b>Хочу константу на ФУРИНУ!!!!</b>')


def voley(request):
    return HttpResponse('<table>Расписание тренировок</table>')
