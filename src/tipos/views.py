from collections import deque, namedtuple
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .servicio import run_test
from .eulerian import calcular_no_dirigido, calcular_dirigido
from .hamilton import calcular_circuito_hamilton


@csrf_exempt
def main(request):
    return render(request, 'tipos/index.html', {})

def main2(request):
    return render(request, 'tipos/index2.html', {})

@api_view(['POST'])
@csrf_exempt
def calcular_tipos(request):
    data = request.data
    # respuestas = run_test(data['nodos'], data['aristas'])

    grafo = {}
    for nodo in data['nodos']:
        grafo[nodo] = []
        for arista in data['aristas']:
            if nodo in arista:
                grafo[nodo].append(list(set(arista) - set([nodo]))[0])
        grafo[nodo] = list(set(grafo[nodo]))

    print(grafo)
    
    respuesta_eurleriano = calcular_no_dirigido(grafo)
    respuesta_hamilton = calcular_circuito_hamilton(data['nodos'], data['aristas'])

    respuestas_dict = {
        'euler': respuesta_eurleriano,
        'hamilton': respuesta_hamilton
    }

    return JsonResponse(respuestas_dict)

@api_view(['POST'])
@csrf_exempt
def calcular_tipos_dirigidos(request):
    data = request.data
    print(data['aristas'])
    respuesta_euleriano = calcular_dirigido(data['nodos'], data['aristas'])
    respuestas_dict = {
        'euler': respuesta_euleriano,
        'hamilton': ''
    }

    return JsonResponse(respuestas_dict)
