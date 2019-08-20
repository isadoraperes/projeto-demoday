from django.urls import path, include
from website.views import home, blog, perfil, login, acessar, cadastrar

urlpatterns = [
    path('', home),
    path('blog', blog),
    path('login', login),
    path('acessar', acessar),
    path('perfil', perfil),
    path('cadastrar', cadastrar),
]
