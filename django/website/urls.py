from django.urls import path, include
from website.views import home, blog, perfil, login, cadastrar

urlpatterns = [
    path('', home),
    path('blog', blog),
    path('login', login),
    path('perfil', perfil),
    path('cadastrar', cadastrar),
]
