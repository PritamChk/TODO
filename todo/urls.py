from todo.views import Registration, login
from django.urls import path


urlpatterns = [
    path('home/',login),
    path('home/registration/',Registration)
]
