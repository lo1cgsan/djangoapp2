from django.urls import path

from . import views
from django.views.generic import ListView
from studenci.models import Miasto

app_name = 'studenci'
urlpatterns = [
	path('', views.index, name='index'),
    path('miasta/lista', ListView.as_view(model=Miasto), name='miasta_lista'),
    path('miasta/', views.miasta, name='miasta'),
    path('miasta/dodaj', views.DodajMiasto.as_view(), name='miasta_dodaj'),
    path('miasta/edytuj/<int:pk>', views.EdytujMiasto.as_view(), name='miasta_edytuj'),
    path('miasta/usun/<int:pk>', views.UsunMiasto.as_view(), name='miasta_usun'),
    path('uczelnie/', views.uczelnie, name='uczelnie'),
    path('uczelnie/lista', views.ListaUczelni.as_view(), name='uczelnie_lista'),
    path('login/', views.login, name='login'),
]
