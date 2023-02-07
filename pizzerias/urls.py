from django.urls import path

from . import views

app_name = 'pizzerias'

urlpatterns = [
    # Home Pages
    path('', views.index, name='index')
]