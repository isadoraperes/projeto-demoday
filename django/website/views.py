from django.shortcuts import render
from website.models import Pessoa, Categoria, Curso

# Create your views here.

#verificar se a home precisa de uma função aqui

#cadastrar novo usuário na plataforma
def cadastrar(request):
    
    context = {}
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.genero = request.POST.get('genero')
        pessoa.idade = request.POST.get('idade')
        pessoa.email = request.POST.get('email')
        pessoa.save()
        context = {'msg': 'Cadastro feito com sucesso!'}
        return render(request, 'perfil.html', context)

    return render(request, 'cadastrar.html', context)

