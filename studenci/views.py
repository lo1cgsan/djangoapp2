from django.shortcuts import render
from django.http import HttpResponse

from studenci.models import Miasto


def index(request):
    return HttpResponse("Witaj w aplikacji Studenci!")
    # return render(request, 'pizza/index.html')


def miasta(request):

    miasta = Miasto.objects.all()
    kontekst = {
        'miasta': miasta
    }

    return render(request, 'studenci/miasta.html', kontekst)
