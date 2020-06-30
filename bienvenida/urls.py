from django.urls import path
from bienvenida import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
