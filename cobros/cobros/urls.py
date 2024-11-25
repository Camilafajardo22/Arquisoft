from django.urls import path
from . import views

urlpatterns = [
    # Otras rutas de tu aplicación
    path('cobros_api/', views.CobrosList, name='lista_cobros'),
    path('cobros/', views.CobrosPage, name='cobros_page'),
    path('suma/', views.obtener_suma_total, name='obtener_suma_total'),  # Nueva ruta
]

