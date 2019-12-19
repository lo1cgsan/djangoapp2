from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from pizza.forms import SkladnikForm
from pizza.models import Skladnik

def index(request):
    # return HttpResponse("Witaj w barze Pizza!")
    return render(request, 'pizza/index.html')


def SkladnikDodaj(request):
    if request.method == 'POST':
        form = SkladnikForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            s = Skladnik(
                nazwa = form.cleaned_data['nazwa'],
                jarski = form.cleaned_data['jarski'],
                cena = form.cleaned_data['cena']
            )
            s.save()
            messages.success(request, "Dane zapisano!")
            return redirect(reverse('pizza:index'))
    else:
        form = SkladnikForm()

    kontekst = {'form': form}

    return render(request, 'pizza/skladnikform.html', kontekst)


def news(request):
    # return HttpResponse("<h1>Nowości w barze</h1>")
    return render(request, 'pizza/news.html')