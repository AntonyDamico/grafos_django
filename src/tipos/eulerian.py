from copy import copy


def esta_conectado(G):
    '''
    esta_conectado - checkea si los nodos del grafo están conectados 
    usando la Busqueda en anchura - Breadth-First Search Algorithm (BFS)
    '''
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


def nodos_grado_impar(G):
    '''
    nodos_grado_impar - devuelve una lista con los nodos de grado impar
    '''
    nodos_grado_impar = []
    for u in G:
        if len(G[u]) % 2 != 0:
            nodos_grado_impar.append(u)
    return nodos_grado_impar


def from_dict(G):
    '''
    from_dict - return a list of tuples links from a graph G in a 
    dictionary format
    '''
    links = []
    for u in G:
        for v in G[u]:
            links.append((u, v))
    return links


def todos_nodos_en_aristas(G):
    '''
    Devuelve verdadero si todos los nodos pertenecen a alguna arista
    '''
    for key in G:
        if not G[key]:
            return False
    return True


def calcular_euleriano_no_dirigido(G):
    '''
    Devuelve el camino o circuito euleriano para un grafo no dirigido
    o no es grafo euleriano en el caso de que no lo sea
    '''
    if len(G) == 1 or not todos_nodos_en_aristas(G):
        return 'No es un grafo euleriano.---'

    respuesta = 'Es un circuito euleriano: '
    nodos_grado_im = nodos_grado_impar(G)
    if len(nodos_grado_im) > 2 or len(nodos_grado_im) == 1:
        return 'No es un grafo euleriano.---'
    elif len(nodos_grado_im) == 2:
        respuesta = 'Es un camino euleriano: '
    g = copy(G)
    camino = []
    if len(nodos_grado_im) == 2:
        u = nodos_grado_im[0]
    else:
        u = list(g)[0]
    while len(from_dict(g)) > 0:
        nodo_actual = u
        for u in g[nodo_actual]:
            g[nodo_actual].remove(u)
            g[u].remove(nodo_actual)
            bridge = not esta_conectado(g)
            if bridge:
                g[nodo_actual].append(u)
                g[u].append(nodo_actual)
            else:
                break
        if bridge:
            g[nodo_actual].remove(u)
            g[u].remove(nodo_actual)
            g.pop(nodo_actual)
        camino.append((nodo_actual, u))

    respuesta += str(camino[0][0]) + " -> "

    for arista in camino:
        respuesta += str(arista[1]) + " -> "

    return respuesta


'''
==============================================
|| Calculando grafos eulerianos dirigidos  ||
==============================================
'''

def calcular_grados(nodos, aristas):
    '''
    Calcula la diferencia entre las aristas de entrada y salida
    de cada nodo
    '''
    grados_arr = [0] * len(nodos)
    for arista in aristas:
        grados_arr[nodos.index(arista[0])] += 1
        grados_arr[nodos.index(arista[1])] -= 1
    return grados_arr

def calcular_euleriano_dirigido(nodos, aristas):
    '''
    Devuelve el camino o circuito euleriano para un grafo dirigido
    o no es grafo euleriano en el caso de que no lo sea
    '''
    if not aristas:
        return "No es un grafo euleriano.---"

    grados_arr = calcular_grados(nodos, aristas)

    # Si la diferencia entre las aristas de entrada y salida de algún nodo
    # es mayor a 1, no es euleriano
    if not all(x == 1 or x == -1 or x == 0 for x in grados_arr):
        print(grados_arr)
        return "No es un grafo euleriano.---"

    # Se empieza por el nodo que tiene mayor cantidad de salidas
    if 1 in grados_arr:
        nodo_actual = nodos[grados_arr.index(1)]
    else:
        for arista in aristas:
            grados_arr[nodos.index(arista[0])] += 1
            grados_arr[nodos.index(arista[1])] += 1
        nodo_actual = nodos[grados_arr.index(max(grados_arr))]

    # Pilas para hacer el algoritmo de Hielholzer
    # https://math.stackexchange.com/questions/1871065/euler-path-for-directed-graph
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
        camino_final_str += nodo + " -> "

    if camino_final[0] == camino_final[-1]:
        return "Es un circuito euleriano: " + camino_final_str
    return "Es un camino euleriano: " + camino_final_str
