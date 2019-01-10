def encontrar_todos_caminos(grafo, inicio, final, camino=[]):
    camino = camino + [inicio]
    if inicio == final:
        return [camino]
    # if not grafo.has_key(start):
    if not inicio in grafo:
        return []
    caminos = []
    for nodo in grafo[inicio]:
        if nodo not in camino:
            nuevos_caminos = encontrar_todos_caminos(grafo, nodo, final, camino)
            for nuevo_camino in nuevos_caminos:
                caminos.append(nuevo_camino)
    return caminos


def calcular_camino(grafo):
    print(grafo)
    ciclos = []
    for nodo_inicio in grafo:
        for nodo_final in grafo:
            nuevos_caminos = encontrar_todos_caminos(grafo, nodo_inicio, nodo_final)
            for camino in nuevos_caminos:
                if (len(camino) == len(grafo)):
                    ciclos.append(camino)
    return ciclos


def calcular_circuito(grafo):
    ciclos = []
    for nodo_inicio in grafo:
        for nodo_final in grafo:
            nuevos_caminos = encontrar_todos_caminos(grafo, nodo_inicio, nodo_final)
            for camino in nuevos_caminos:
                if (len(camino) == len(grafo)):
                    if camino[0] in grafo[camino[len(grafo)-1]]:
                        # print camino[0], grafo[camino[len(grafo)-1]]
                        camino.append(camino[0])
                        ciclos.append(camino)
    return ciclos


def parse_respuesta(respuesta):
    respuesta_str = ''
    for nodo in respuesta:
        respuesta_str += nodo + ' -> '
    return respuesta_str


def calcular_hamilton(grafo):
    respuesta = calcular_circuito(grafo)
    if respuesta:
        respuesta_str = parse_respuesta(respuesta[0])
        return 'Es un circuito hamiltoniano: ' + respuesta_str

    respuesta = calcular_camino(grafo)
    if not respuesta or len(respuesta[0]) == 1:
        return 'No es un grafo hamiltoniano.---'

    respuesta_str = parse_respuesta(respuesta[0])
    return 'Es un camino hamiltoniano: ' + respuesta_str
    # return 'No es un grafo hamiltoniano'

# from collections import defaultdict


# class grafo2():
#     def __init__(self, vertices):
#         lengt_v = len(vertices)
#         self.grafo = [[0 for column in range(lengt_v)]
#                       for row in range(lengt_v)]
#         self.nodos = vertices
#         self.V = lengt_v
#         self.camino = []

#     ''' Check if this vertex is an adjacent vertex
# 		of the previously added vertex and is not
# 		included in the camino earlier '''

#     def isSafe(self, v, pos, camino):
#         # Check if current vertex and last vertex
#         # in camino are adjacent
#         if self.grafo[camino[pos-1]][v] == 0:
#             return False

#         # Check if current vertex not already in camino
#         for vertex in camino:
#             if vertex == v:
#                 return False

#         return True

#     # A recursive utility function to solve
#     # hamiltonian cycle problem
#     def hamCycleUtil(self, camino, pos):

#         # base case: if all vertices are
#         # included in the camino
#         if pos == self.V:
#             # Last vertex must be adjacent to the
#             # first vertex in camino to make a cyle
#             if self.grafo[camino[pos-1]][camino[0]] == 1:
#                 return True
#             else:
#                 return False

#         # Try different vertices as a next candidate
#         # in Hamiltonian Cycle. We don't try for 0 as
#         # we included 0 as starting point in in hamCycle()
#         for v in range(1, self.V):

#             if self.isSafe(v, pos, camino) == True:

#                 camino[pos] = v

#                 if self.hamCycleUtil(camino, pos+1) == True:
#                     return True

#                 # Remove current vertex if it doesn't
#                 # lead to a solution
#                 camino[pos] = -1

#         return False

#     def hamCycle(self):
#         if self.V == 2:
#             return f"Es un camino hamiltoniano: {self.nodos[0]} {self.nodos[1]}"

#         camino = [-1] * self.V

#         ''' Let us put vertex 0 as the first vertex
# 			in the camino. If there is a Hamiltonian Cycle,
# 			then the camino can be started from any point
# 			of the cycle as the grafo is undirected '''
#         camino[0] = 0

#         if self.hamCycleUtil(camino, 1) == False:
#             return "No es un circuito hamiltoniano"

#         self.printSolution(camino)
#         resultado = "Es un circuito hamiltoniano: "
#         for nodo in self.camino:
#             resultado += nodo + " "
#         return resultado

#     def printSolution(self, camino):
#         for vertex in camino:
#             self.camino.append(self.nodos[vertex])
#         self.camino.append(self.nodos[camino[0]])

#     def crear_matriz(self, nodos, aristas):
#         matriz = [[0] * len(nodos) for i in range(len(nodos))]
#         for arista in aristas:
#             i, j = arista[0], arista[1]
#             i, j = nodos.index(i), nodos.index(j)
#             matriz[i][j] += 1
#         return matriz

#     def set_grafo(self, nodos, aristas):
#         self.grafo = self.crear_matriz(nodos, aristas)


# g1.set_grafo = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
# 			[0, 1, 0, 0, 1,],[1, 1, 0, 0, 1],
# 			[0, 1, 1, 1, 0], ]

# def calcular_circuito_hamilton(nodos, aristas):
#     grafo = grafo2(nodos)
#     grafo.set_grafo(nodos, aristas)
#     return grafo.hamCycle()


# nodos = ['A','B','C','D']
# aristas = [
# 	['A','B'],
# 	['B','C'],
# 	['C','D'],
# 	['D','A'],
# ]

# g1 = grafo(nodos)
# g1.set_grafo(nodos, aristas)

# print(g1.hamCycle())


# g2 = grafo(5)
# g2.grafo = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
# 		[0, 1, 0, 0, 1,], [1, 1, 0, 0, 0],
# 		[0, 1, 1, 0, 0], ]

# Print the solution
# print(g2.hamCycle())

# grafo = {
#     'A': ['B'],
#     'B': ['A'],
# }





# print("Finding Hamiltonian caminos----")

# a = calcular_circuito(grafo)
# print(a)
