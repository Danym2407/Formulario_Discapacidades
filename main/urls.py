from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cuestionario/', views.cuestionario_view, name='cuestionario'),
]
