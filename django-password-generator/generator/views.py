from lib2to3.pgen2.pgen import generate_grammar
import random

from django.shortcuts import render

#from django.http import HttpResponse


def about(request):
  return  render(request, 'about.html')# devuelve un html


def home(request):
    return render(request, 'home.html')# lo que va en '' es la direccion de la carpeta en el caso de tener otra iria : 'vistas/home.html'


def password (request) :

    character =  list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''

    lenght= int(request.GET.get('lenght'))
    if request.GET.get('uppercase'):
        character.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get('special'):
        character.extend(list("-_!@#$%*()+^"))
    if request.GET.get('numbers'):
        character.extend(list("1234567890"))




    for x in range(lenght):
        generated_password += random.choice(character)

    return render(request, 'password.html', {'password': generated_password})
