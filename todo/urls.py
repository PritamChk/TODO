from todo.views import login
from django.urls import path


urlpatterns = [
    path('home/',login)
]
