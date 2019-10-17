from django.shortcuts import render
from django.http import HttpResponse

from studenci.models import Miasto


def index(request):
    return HttpResponse("Witaj w aplikacji Studenci!")
    # return render(request, 'pizza/index.html')


def miasta(request):

    if request.method == 'POST':
        nazwa = request.POST.get('nazwa')
        kod = request.POST.get('kod')
        m = Miasto(nazwa=nazwa, kod=kod)
        m.save()

    miasta = Miasto.objects.all()
    kontekst = {
        'miasta': miasta
    }

    return render(request, 'studenci/miasta.html', kontekst)
