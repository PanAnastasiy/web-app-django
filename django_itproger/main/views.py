from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def genshin(request):
    return HttpResponse('<b>Хочу константу на ФУРИНУ!!!!</b>')


def voley(request):
    return HttpResponse('<table>Расписание тренировок</table>')
