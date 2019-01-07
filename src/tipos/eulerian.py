from copy import copy

'''

	esta_conectado - Checks if a graph in the form of a dictionary is 
	connected or not, using Breadth-First Search Algorithm (BFS)

'''


def esta_conectado(G):
    nodo_inicio = list(G)[0]
    color = {v: 'white' for v in G}
    color[nodo_inicio] = 'gray'
    S = [nodo_inicio]
    while len(S) != 0:
        u = S.pop()
        for v in G[u]:
            if color[v] == 'white':
                color[v] = 'gray'
                S.append(v)
            color[u] = 'black'
    return list(color.values()).count('black') == len(G)


'''
	odd_degree_nodes - returns a list of all G odd degrees nodes
'''


def odd_degree_nodes(G):
    odd_degree_nodes = []
    for u in G:
        if len(G[u]) % 2 != 0:
            odd_degree_nodes.append(u)
    return odd_degree_nodes


'''
	from_dict - return a list of tuples links from a graph G in a 
	dictionary format
'''


def from_dict(G):
    links = []
    for u in G:
        for v in G[u]:
            links.append((u, v))
    return links


'''
	fleury(G) - return eulerian trail from graph G or a 
	string 'Not Eulerian Graph' if it's not possible to trail a path
'''


def calcular_no_dirigido(G):
    '''
            checks if G has eulerian cycle or trail
    '''
    if len(G) == 1:
        return 'No es un grafo euleriano'

    respuesta = 'Es un circuito euleriano: '
    odn = odd_degree_nodes(G)
    if len(odn) > 2 or len(odn) == 1:
        return 'No es un grafo euleriano'
    elif len(odn) == 2:
        respuesta = 'Es un camino euleriano: '
    g = copy(G)
    trail = []
    if len(odn) == 2:
        u = odn[0]
    else:
        u = list(g)[0]
    while len(from_dict(g)) > 0:
        current_vertex = u
        for u in g[current_vertex]:
            g[current_vertex].remove(u)
            g[u].remove(current_vertex)
            bridge = not esta_conectado(g)
            if bridge:
                g[current_vertex].append(u)
                g[u].append(current_vertex)
            else:
                break
        if bridge:
            g[current_vertex].remove(u)
            g[u].remove(current_vertex)
            g.pop(current_vertex)
        trail.append((current_vertex, u))

    respuesta += str(trail[0][0]) + " "

    for arista in trail:
        respuesta += str(arista[1]) + " "

    # respuesta += str(trail)
    return respuesta

# testing seven bridges of konigsberg
# print('Konigsberg')
# G = {0: [2, 2, 3], 1: [2, 2, 3], 2: [0, 0, 1, 1, 3], 3: [0, 1, 2]}
# print(fleury(G))

# # testing an eulerian cycle
# print('1st Eulerian Cycle')
# G = {0: [1, 4, 6, 8], 1: [0, 2, 3, 8], 2: [1, 3], 3: [1, 2, 4, 5], 4: [0, 3], 5: [3, 6], 6: [0, 5, 7, 8], 7: [6, 8], 8: [0, 1, 6, 7]}
# print(fleury(G))

# # testing another eulerian cycle
# print('2nd Eulerian Cycle')
# G = {1: [2, 3, 4, 4], 2: [1, 3, 3, 4], 3: [1, 2, 2, 4], 4: [1, 1, 2, 3]}
# G = {'A': ['B'], 'B': ['C'], 'C': ['A']}
# print(calcular_no_dirigido(G))

# # testing an eulerian trail
# print('Eulerian Trail')
# G = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}
# print(fleury(G))


# def calcular_dirigido(nodos, aristas):
# 	grados = dict((nodo, []) for nodo in nodos)
# 	for nodo in nodos:
# 		pass


# {'A': ['B', 'C', 'D'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'A', 'C']}


def calcular_dirigido(nodos, aristas):
    grados_arr = [0] * len(nodos)
    for arista in aristas:
        grados_arr[nodos.index(arista[0])] += 1
        grados_arr[nodos.index(arista[1])] -= 1

    if not all(x == 1 or x == -1 or x == 0 for x in grados_arr):
        print(grados_arr)
        return "No es un grafo euleriano"

    # nodo_actual = nodos[1]
    if 1 in grados_arr:
        nodo_actual = nodos[grados_arr.index(1)]
    else:
        for arista in aristas:
            grados_arr[nodos.index(arista[0])] += 1
            grados_arr[nodos.index(arista[1])] += 1
        nodo_actual = nodos[grados_arr.index(max(grados_arr))]

    camino_temporal = [nodo_actual]
    camino_final = []

    while camino_temporal:
        nueva_arista = [
            sub_arista for sub_arista in aristas if nodo_actual == sub_arista[0]
        ]
        if nueva_arista:
            nuevo_nodo = nueva_arista[0][1]
            camino_temporal.append(nuevo_nodo)
            nodo_actual = nuevo_nodo
            aristas.remove(nueva_arista[0])
        else:
            nodo_actual = camino_temporal.pop()
            # camino_final.append(nodo_actual)
            camino_final.insert(0, nodo_actual)
    # camino_final.reverse()
    camino_final_str = ''
    for nodo in camino_final:
        camino_final_str += nodo + " "

    if camino_final[0] == camino_final[-1]:
        return "Es un circuito euleriano: " + camino_final_str
    return "Es un camino euleriano: " + camino_final_str

# nodos = ['A', 'B', 'C', 'D', 'E']
# aristas = [['B', 'A'], ['A', 'D'], ['D', 'B'], ['B', 'C'], ['C', 'E'], ['E', 'B']]
# print(calcular_dirigido(nodos, aristas))
