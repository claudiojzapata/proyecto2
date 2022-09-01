from django.shortcuts import render
from django.http import HttpResponse 
from .models import Curso 
# Create your views here.

def curso(request):
    curso=Curso(nombre="Curso de Python", comision=123456)
    curso.save
    texto =f"Curso Creado: nombre: {curso.nombre} comision: {curso.comision}"
    return HttpResponse(texto)




def inicio(request):

      return HttpResponse("Pagina de inicio")



def estudiantes(request):

      return HttpResponse("Pagina de estudiantes")


def entregables(request):

      return HttpResponse("Pagina de entregables")


def cursos(request):

    return HttpResponse("Pagina de cursos")

     

def profesores(request):

    return HttpResponse("Pagina de profesores")

      




