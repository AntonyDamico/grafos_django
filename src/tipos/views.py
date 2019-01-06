from collections import deque, namedtuple
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .servicio import run_test


@csrf_exempt
def main(request):
    return render(request, 'tipos/index.html', {})

def main2(request):
    return render(request, 'tipos/index2.html', {})

@api_view(['POST'])
@csrf_exempt
def calcular_tipos(request):
    data = request.data

    respuestas = run_test(data['nodos'], data['aristas'])
    respuestas_dict = {
        'euler': respuestas[0],
        'hamilton': respuestas[1]
    }

    return JsonResponse(respuestas_dict)
