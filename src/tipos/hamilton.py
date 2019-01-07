# Python program for solution of
# hamiltonian cycle problem

# from collections import defaultdict


# class Graph2():
#     def __init__(self, vertices):
#         lengt_v = len(vertices)
#         self.graph = [[0 for column in range(lengt_v)]
#                       for row in range(lengt_v)]
#         self.nodos = vertices
#         self.V = lengt_v
#         self.camino = []

#     ''' Check if this vertex is an adjacent vertex
# 		of the previously added vertex and is not
# 		included in the path earlier '''

#     def isSafe(self, v, pos, path):
#         # Check if current vertex and last vertex
#         # in path are adjacent
#         if self.graph[path[pos-1]][v] == 0:
#             return False

#         # Check if current vertex not already in path
#         for vertex in path:
#             if vertex == v:
#                 return False

#         return True

#     # A recursive utility function to solve
#     # hamiltonian cycle problem
#     def hamCycleUtil(self, path, pos):

#         # base case: if all vertices are
#         # included in the path
#         if pos == self.V:
#             # Last vertex must be adjacent to the
#             # first vertex in path to make a cyle
#             if self.graph[path[pos-1]][path[0]] == 1:
#                 return True
#             else:
#                 return False

#         # Try different vertices as a next candidate
#         # in Hamiltonian Cycle. We don't try for 0 as
#         # we included 0 as starting point in in hamCycle()
#         for v in range(1, self.V):

#             if self.isSafe(v, pos, path) == True:

#                 path[pos] = v

#                 if self.hamCycleUtil(path, pos+1) == True:
#                     return True

#                 # Remove current vertex if it doesn't
#                 # lead to a solution
#                 path[pos] = -1

#         return False

#     def hamCycle(self):
#         if self.V == 2:
#             return f"Es un camino hamiltoniano: {self.nodos[0]} {self.nodos[1]}"

#         path = [-1] * self.V

#         ''' Let us put vertex 0 as the first vertex
# 			in the path. If there is a Hamiltonian Cycle,
# 			then the path can be started from any point
# 			of the cycle as the graph is undirected '''
#         path[0] = 0

#         if self.hamCycleUtil(path, 1) == False:
#             return "No es un circuito hamiltoniano"

#         self.printSolution(path)
#         resultado = "Es un circuito hamiltoniano: "
#         for nodo in self.camino:
#             resultado += nodo + " "
#         return resultado

#     def printSolution(self, path):
#         for vertex in path:
#             self.camino.append(self.nodos[vertex])
#         self.camino.append(self.nodos[path[0]])

#     def crear_matriz(self, nodos, aristas):
#         matriz = [[0] * len(nodos) for i in range(len(nodos))]
#         for arista in aristas:
#             i, j = arista[0], arista[1]
#             i, j = nodos.index(i), nodos.index(j)
#             matriz[i][j] += 1
#         return matriz

#     def set_graph(self, nodos, aristas):
#         self.graph = self.crear_matriz(nodos, aristas)


# g1.set_graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
# 			[0, 1, 0, 0, 1,],[1, 1, 0, 0, 1],
# 			[0, 1, 1, 1, 0], ]

# def calcular_circuito_hamilton(nodos, aristas):
#     grafo = Graph2(nodos)
#     grafo.set_graph(nodos, aristas)
#     return grafo.hamCycle()


# nodos = ['A','B','C','D']
# aristas = [
# 	['A','B'],
# 	['B','C'],
# 	['C','D'],
# 	['D','A'],
# ]

# g1 = Graph(nodos)
# g1.set_graph(nodos, aristas)

# print(g1.hamCycle())


# g2 = Graph(5)
# g2.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
# 		[0, 1, 0, 0, 1,], [1, 1, 0, 0, 0],
# 		[0, 1, 1, 0, 0], ]

# Print the solution
# print(g2.hamCycle())

# graph = {
#     'A': ['B'],
#     'B': ['A'],
# }


def encontrar_todos_caminos(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    # if not graph.has_key(start):
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = encontrar_todos_caminos(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def calcular_camino(graph):
    print(graph)
    cycles = []
    for startnode in graph:
        for endnode in graph:
            newpaths = encontrar_todos_caminos(graph, startnode, endnode)
            for path in newpaths:
                if (len(path) == len(graph)):
                    cycles.append(path)
    return cycles


def calcular_circuito(graph):
    cycles = []
    for startnode in graph:
        for endnode in graph:
            newpaths = encontrar_todos_caminos(graph, startnode, endnode)
            for path in newpaths:
                if (len(path) == len(graph)):
                    if path[0] in graph[path[len(graph)-1]]:
                        # print path[0], graph[path[len(graph)-1]]
                        path.append(path[0])
                        cycles.append(path)
    return cycles


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


# print("Finding Hamiltonian Paths----")

# a = calcular_circuito(graph)
# print(a)
