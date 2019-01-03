from collections import deque, namedtuple
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response


@csrf_exempt
def main(request):
    return render(request, 'tipos/index.html', {})


@api_view(['POST'])
@csrf_exempt
def calcular_tipos(request):
    data = request.data
    return JsonResponse({"camino": "123", "peso": 2})
    print("data!!!!!: ", data, type(data))
    aristas = [tuple(arista) for arista in data['aristas']]
    nodos = data['nodos']
    # grafo = Grafo(aristas)
    inicio, destino = data['inicio'], data['destino']

    if inicio not in nodos or destino not in nodos:
        return JsonResponse({'camino':'Use nodos que estén en pantalla'})

    esta_inicio = [item for item in aristas if inicio in item]
    esta_destino = [item for item in aristas if destino in item]
    
    if not esta_inicio or not esta_destino:
        return JsonResponse({'camino':'Use nodos que estén conectados con aristas'})


    # camino, peso = grafo.dijkstra(data['inicio'], data['destino'])
    # camino_str = ''
    # for elemento in camino:
    #     camino_str += ' ' + elemento + ','

    # print(camino_str[:-1])
    # respuesta = {
    #     'camino': camino_str[:-1],
    #     'peso': peso
    # }
    # return JsonResponse(respuesta)
    return JsonResponse({})