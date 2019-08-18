from django.urls import path, include
from website.views import login, cadastrar, perfil, blog

urlpatterns = [
    path('login', login),
    path('cadastrar', cadastrar),
    path('perfil', perfil)
    path('blog', blog)
]
