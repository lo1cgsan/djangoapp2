from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from studenci.models import Miasto, Uczelnia


def index(request):
    return HttpResponse("Witaj w aplikacji Studenci!")
    # return render(request, 'pizza/index.html')


def miasta(request):
    if request.method == 'POST':
        nazwa = request.POST.get('nazwa')
        kod = request.POST.get('kod')
        if len(nazwa.strip()):
            m = Miasto(nazwa=nazwa, kod=kod)
            m.save()
            messages.success(request, "Dane zapisano!")
        else:
            messages.error(request, "Błędne dane!")

    miasta = Miasto.objects.all()
    kontekst = {
        'miasta': miasta
    }

    return render(request, 'studenci/miasta.html', kontekst)


def uczelnie(request):

    if request.method == 'POST':
        nazwa = request.POST.get('nazwa')
        u = Uczelnia(nazwa=nazwa)
        u.save()

    uczelnie = Uczelnia.objects.all()
    kontekst = {
        'uczelnie': uczelnie
    }

    return render(request, 'studenci/uczelnie.html', kontekst)
