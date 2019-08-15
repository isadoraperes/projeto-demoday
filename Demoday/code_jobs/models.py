from django.db import models

# Create your models here.

class Pessoa(models.Model):
    GENEROS = (
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
      nome = models.CharField(
        max_length=255,
        verbose_name='Nome'
    )
    sobrenome = models.CharField(
        max_length=255,
        verbose_name='Sobrenome'
    )
     genero = models.CharField(
        max_length=255,
        verbose_name='Gênero',
        choices=GENEROS
    )
      email = models.EmailField(
        max_length=255,
        verbose_name='E-mail'
    )
    idade = models.CharField(
        max_length=2,
        verbose_name= 'Idade'
    )
class Categoria(models.Model):
    CATEGORIAS = (
        ('FRONT_END' , 'Curso de Front End'),
        ('BACK_END' , 'Curso de Back End'),
        ('BANCO_DE_DADOS' , 'Curso de Banco de dados'),

#TABELAS? RELACIONAR AO BANCO DE DADOS


    )
class Curso(models.Model):
    CURSO = (
        ('BASICO' , 'Nível básico' ),
        ('INTERMEDIARIO' , 'Nível intermediário' ),
        ('AVANCADO' , 'Nível avançado' ),

    )
#TABELAS? RELACIONAR AO BANCO DE DADOS


     # Aqui coloquei uma data_de_acesso
    data_de_acesso = models.DateTimeField(auto_now_add=True)
    # ativo = models.BooleanField(default=True)