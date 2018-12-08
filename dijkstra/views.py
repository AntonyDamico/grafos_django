from collections import deque, namedtuple
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response


@csrf_exempt
def main(request):
    print(request)
    return render(request, 'dijkstra/index.html', {})


@api_view(['POST'])
@csrf_exempt
def dijkstra(request):
    data = request.data
    aristas = [tuple(arista) for arista in data['aristas']]
    nodos = data['nodos']
    grafo = Grafo(aristas)
    inicio, destino = data['inicio'], data['destino']

    if inicio not in nodos or destino not in nodos:
        return JsonResponse({'camino':'Use nodos que estén en pantalla'})

    camino = grafo.dijkstra(data['inicio'], data['destino'])
    camino_str = ''
    for elemento in camino:
        camino_str += ' ' + elemento + ','

    esta_inicio = [item for item in aristas if inicio in item]
    esta_destino = [item for item in aristas if destino in item]
    
    if not esta_inicio or not esta_destino:
        return JsonResponse({'camino':'Use nodos que estén conectados con aristas'})

    print(camino_str[:-1])
    respuesta = {
        'camino': camino_str[:-1]
    }
    return JsonResponse(respuesta)


'''
DIJKSTRA
'''


# infinito para la distancia a nodos que no son vecinos
inf = float('inf')
Arista = namedtuple('Arista', 'origen, final, peso')


def hacer_arista(origen, final, peso=1):
    return Arista(origen, final, int(peso))


class Grafo:
    def __init__(self, aristas):
        # comprueba si los datos que se pasaron son validos
        aristas_error = [i for i in aristas if len(i) not in [2, 3]]
        if aristas_error:
            raise ValueError('Wrong edges data: {}'.format(aristas_error))

        self.aristas = [hacer_arista(*arista) for arista in aristas]

    @property
    def vertices(self):
        # Devuelve una lista de todos los vertices
        return set(
            sum(
                ([arista.origen, arista.final] for arista in self.aristas), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def quitar_arista(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        aristas = self.aristas[:]
        for arista in aristas:
            if [arista.origen, arista.final] in node_pairs:
                self.aristas.remove(arista)

    def agregar_arista(self, n1, n2, peso=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for arista in self.aristas:
            if [arista.origen, arista.final] in node_pairs:
                return ValueError('Arista {} {} ya existe'.format(n1, n2))

        self.aristas.append(Arista(origen=n1, final=n2, peso=peso))
        if both_ends:
            self.aristas.append(Arista(origen=n2, final=n1, peso=peso))

    @property
    def vecinos(self):
        # Crea los vecinos de cada nodo
        vecinos = {vertice: set() for vertice in self.vertices}
        for arista in self.aristas:
            vecinos[arista.origen].add((arista.final, arista.peso))
            vecinos[arista.final].add((arista.origen, arista.peso))

        return vecinos

    def dijkstra(self, iniccio, destino):
        # Comprueba que el origen esta en la lista de vertices
        assert iniccio in self.vertices, 'El nodo de inicio no existe'
        # Da distancia infinita a todos los vertices
        distancias = {vertice: inf for vertice in self.vertices}
        # Le pone vertice anterior None a todos los vertices
        vertices_previos = {
            vertice: None for vertice in self.vertices
        }
        # Da distancia 0 desde el origen a el mismo
        distancias[iniccio] = 0
        vertices = self.vertices.copy()

        while vertices:
            print(vertices)
            # Te da el vertice al que hay menor distancia
            vertice_actual = min(
                vertices, key=lambda vertice: distancias[vertice])
            vertices.remove(vertice_actual)

            if distancias[vertice_actual] == inf:
                break

            # Asigna valores de distancia para cada vecino del vertice actual
            for vecino, peso in self.vecinos[vertice_actual]:
                ruta_alternativa = distancias[vertice_actual] + peso
                if ruta_alternativa < distancias[vecino]:
                    distancias[vecino] = ruta_alternativa
                    vertices_previos[vecino] = vertice_actual

        camino, vertice_actual = deque(), destino
        # Arma el camino final
        while vertices_previos[vertice_actual] is not None:
            camino.appendleft(vertice_actual)
            vertice_actual = vertices_previos[vertice_actual]
        # Le da el vertice inicial al camino
        if camino:
            camino.appendleft(vertice_actual)
        return camino
