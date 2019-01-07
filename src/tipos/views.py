from collections import deque, namedtuple
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from copy import copy

from .servicio import run_test
from .eulerian import calcular_euleriano_no_dirigido, calcular_euleriano_dirigido
from .hamilton import calcular_hamilton


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

 
    respuesta_hamilton = calcular_hamilton(grafo)
    respuesta_eurleriano = calcular_euleriano_no_dirigido(grafo)
    
    respuestas_dict = {
        'euler': respuesta_eurleriano,
        'hamilton': respuesta_hamilton
    }

    return JsonResponse(respuestas_dict)

@api_view(['POST'])
@csrf_exempt
def calcular_tipos_dirigidos(request):
    data = request.data
    # print(data['nodos'], data['aristas'])
    # respuesta_hamilton = calcular_circuito_hamilton(data['nodos'], data['aristas'])

    grafo = {}
    for nodo in data['nodos']:
        print('57!!!', nodo)
        grafo[nodo] = []
        for arista in data['aristas']:
            print(nodo, arista, nodo == arista[0])
            if nodo == arista[0]:
                grafo[nodo].append(arista[1])

    print('grafo di', grafo)

    respuesta_hamilton = calcular_hamilton(grafo)
    respuesta_euleriano = calcular_euleriano_dirigido(data['nodos'], data['aristas'])

    respuestas_dict = {
        'euler': respuesta_euleriano,
        'hamilton': respuesta_hamilton
    }

    return JsonResponse(respuestas_dict)
