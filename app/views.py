from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from . models import Project

# Create your views here.


def home(request, id):
    result = id + 100 * 2
    return HttpResponse(f'{result}')


def projects(request):
    proyectos = list(Project.objects.values())
    return JsonResponse({
        "nombre":"de"
    })


def buscar_proyecto(request, id):
    return HttpResponse(f'ID Proyecto: {id}')
