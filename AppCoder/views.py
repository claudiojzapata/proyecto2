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

      return render(request, "AppCoder/inicio.html")



def estudiantes(request):

      return render(request, "AppCoder/estudiantes.html")


def entregables(request):

      return render(request, "AppCoder/entregables.html")




def cursos (request):
      curso1=Curso(nombre="Cursito de Python",comicion=31100)
      curso1.save()
      curso2=Curso(nombre="Cursito de Django",comicion=31101)
      curso2.save()
      lista=[curso1, curso2]
      return render(request, "AppCoder/cursos.html" , {"listita":lista})


     

def profesores(request):

    return render(request, "AppCoder/profesores.html")

      




