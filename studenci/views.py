from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse

from studenci.models import Miasto, Uczelnia
from studenci.forms import StudentLoginForm, UczelniaForm, MiastoForm, MiastoModelForm

from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

def index(request):
    # return HttpResponse("Witaj w aplikacji Studenci!")
    return render(request, 'studenci/index.html')


def miasta(request):
    if request.method == 'POST':
        form = MiastoForm(request.POST)
        # nazwa = request.POST.get('nazwa')
        # kod = request.POST.get('kod')
        # if len(nazwa.strip()):
        if form.is_valid():
            m = Miasto(nazwa=form.cleaned_data['nazwa'], kod=form.cleaned_data['kod'])
            m.save()
            messages.success(request, "Dane zapisano!")
            return redirect(reverse('studenci:miasta'))
        else:
            messages.error(request, "Błędne dane!")
    else:
        form = MiastoForm()

    miasta = Miasto.objects.all()
    kontekst = {
        'miasta': miasta,
        'form': form
    }

    return render(request, 'studenci/miasta.html', kontekst)


def uczelnie(request):

    if request.method == 'POST':
        form = UczelniaForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            u = Uczelnia(nazwa=form.cleaned_data['nazwa'])
            u.save()
            messages.success(request, "Dane zapisano!")
            # przekierowanie
            return redirect(reverse('studenci:uczelnie'))
    else:
        form = UczelniaForm()

    uczelnie = Uczelnia.objects.all()
    kontekst = {
        'form': form,
        'uczelnie': uczelnie
    }

    if request.user.has_perm('studenci.add_uczelnia'):
        return render(request, 'studenci/uczelnie.html', kontekst)
    else:
        messages.info(request, "Nie możesz dodawać uczelni.")
        return redirect(reverse('studenci:index'))


def login(request):
    if request.method == 'POST':
        pass
    else:
        form = StudentLoginForm()

    kontekst = { 'form': form }
    return render(request, 'studenci/login.html', kontekst)


class ListaUczelni(ListView):
    model = Uczelnia
    context_object_name = 'uczelnie'
    template_name = 'studenci/lista_uczelni.html'


@method_decorator(login_required, name='dispatch')
class DodajMiasto(CreateView):
    model = Miasto
    fields = ('nazwa', 'kod')
    template_name = 'studenci/miasto_dodaj.html'
    success_url = reverse_lazy('studenci:miasta_lista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['miasta'] = Miasto.objects.all()
        return context

    def form_valid(self, form):
        messages.success(self.request, "Dodano miasto!")
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EdytujMiasto(SuccessMessageMixin, UpdateView):
    model = Miasto
    form_class = MiastoModelForm
    template_name = 'studenci/miasto_dodaj.html'
    success_url = reverse_lazy('studenci:miasta_lista')
    success_message = 'Zaktualizowano miasto!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['miasta'] = Miasto.objects.all()
        return context


class UsunMiasto(DeleteView):
    model = Miasto
    success_url = reverse_lazy('studenci:miasta_lista')