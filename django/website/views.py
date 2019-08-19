from django.shortcuts import render
from website.models import Pessoa, Categoria, Curso

# Create your views here.

#subir a home
def home(request):
    context = {}
    return render(request, 'home.html', context)

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

def login(request):

    if request.method == 'POST':
        email_acesso = request.POST.get('email')
        pessoa = Pessoa.objects.filter(email=email_acesso).first()

        if pessoa is None:
            context = {'msg':'Cadastre-se para acesso ao site'}
            return render(request,'cadastrar.html', context)
        else:
            context = {'email' : pessoa}
            return render(request, 'perfil.html', context)
    return render(request, 'login.html', {})
#     context = {}
#     if request.method == 'POST'
#         pessoa_email = request.POST.get('email')
#         bd_email = Pessoa.objects.filter(email=pessoa_email).first()
#         if bd_email is not None:
#              argumento = {
#             'pessoa': bd_email
#             }
#          return render(request, 'cadastrar.html',argumento)
#         return render(request, 'login.html',{'msg' : 'Invalido'})
#     return render(request, 'login.html', context)

# def perfil(request):

#     context = {}



