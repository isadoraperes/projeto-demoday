from django.urls import path, include
from website.views import home, login, cadastrar

urlpatterns = [
    path('', home),
    path('login', login),
    path('cadastrar', cadastrar),
]
