from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Witaj w aplikacji Studenci!")
    # return render(request, 'pizza/index.html')


def miasta(request):
    return render(request, 'studenci/miasta.html')
