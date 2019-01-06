from collections import deque, namedtuple
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .servicio import run_test
from .eulerian import calcular_no_dirigido


@csrf_exempt
def main(request):
    return render(request, 'tipos/index.html', {})

def main2(request):
    return render(request, 'tipos/index2.html', {})

@api_view(['POST'])
@csrf_exempt
def calcular_tipos(request):
    data = request.data
    print("data:\nNodos:", data['nodos'],"\nAristas:", data['aristas'])
    respuestas = run_test(data['nodos'], data['aristas'])

    grafo = {}
    for nodo in data['nodos']:
        grafo[nodo] = []
        for arista in data['aristas']:
            if nodo in arista:
                grafo[nodo].append(list(set(arista) - set([nodo]))[0])
        grafo[nodo] = list(set(grafo[nodo]))
    
    respuesta_eurleriano = calcular_no_dirigido(grafo)

    respuestas_dict = {
        'euler': respuesta_eurleriano,
        'hamilton': respuestas[1]
    }

    return JsonResponse(respuestas_dict)
