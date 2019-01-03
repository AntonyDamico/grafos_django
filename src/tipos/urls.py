from django.urls import path

from . import views

app_name = 'tipos'

urlpatterns = [
    path('', views.main, name='main'),
    path('calcular', views.calcular_tipos, name='calcular')
]