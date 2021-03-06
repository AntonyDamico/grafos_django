from django.urls import path

from . import views

app_name = 'tipos'

urlpatterns = [
    path('', views.main, name='main'),
    path('dirigidos', views.main2, name='main2'),
    path('calcular', views.calcular_tipos, name='calcular'),
    path('calcular-dirigido', views.calcular_tipos_dirigidos, name='calcular-dirigidos')
]