from django.urls import path

from . import views

app_name = 'pizza'
urlpatterns = [
	path('', views.index, name='index'),
    path('skladnik/dodaj', views.SkladnikDodaj, name='skladnik_add'),
]
