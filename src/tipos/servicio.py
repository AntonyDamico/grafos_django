def buscar_grados_impares(lista):
	"""Retorna un booleano que indica si hay o no grados impares en el grafo e 
	indica cuantos grados impares hay en caso que si halla"""
	noGradoImpar,numGradosImpares = True,0
	for grado in lista:
		if grado % 2 != 0:
			noGradoImpar = False
			numGradosImpares += 1
	return noGradoImpar,numGradosImpares

def calcular_grados(matriz):
	"""Crea una lista con los grados de cada nodo"""
	lista = []
	for i in range(len(matriz)):
		suma = 0
		suma = grado_nodo(matriz,i)
		lista.append(suma)
	return lista

def euler(matriz,grados):
	"""Calcula si el grafo contiene circuito o camino euleriano"""
	sinGradoImpar, numGradosImpares = buscar_grados_impares(grados)
	if (sinGradoImpar):
		return "Existe camino y circuito euleriano"
	elif(numGradosImpares == 2):
		return "No existe circuito euleriano, sin embargo si existe camino"
	else: 
		return "No existe ni camino ni ciclo euleriano"
	
	print(grados)

def hamilton(grados):
	"""Calcula si el grafo contiene circuito o camino hamiltoniano"""
	maximo = 0
	condicion = len(grados) - 1
	for i in range(len(grados) - 1):
		for j in range(i + 1,len(grados)):
			suma = grados[i] + grados[j]
			maximo = max(maximo,suma)
	if maximo > condicion: return 'Existe camino y circuito hamiltoniano'
	return 'No existe circuito ni camino hamiltoniano'


def grado_nodo(matriz,pos):
	"""Retorna el grado de un nodo dada su posicion y la matriz adyacencia"""
	suma = 0
	for i in range(len(matriz[pos])):
		suma +=  matriz[pos][i]
	return suma


def grafo_conexo(matriz):
	"""Dada una matriz de adyacencia determina si el grafo es conexo"""
	conectados = dict()
	no_conectados = dict()
	for i in range(len(matriz)):
		conectados[i] = []
		no_conectados[i] = []
		for j in range(len(matriz)):
			if i == j:
				continue
			conectados[i].append(j) if matriz[i][j] > 0 else no_conectados[i].append(j)
	
	lista_aux = []
	conexo = True
	bandera = True
	for nodo in conectados:
		while bandera and len(conectados[nodo]) < len(matriz) - 1:
			bandera = False
			lista_aux = conectados[nodo] 
			for n in lista_aux:
				ext = conectados[n]
				for e in ext: 
					if e not in conectados[nodo] and e != nodo:
						conectados[nodo].append(e)
						bandera = True
		result =  all(elem in conectados[nodo]  for elem in no_conectados[nodo])
		conexo = conexo and result
	return conexo

def crear_matriz(nodos,aristas):
	matriz = [[0] * len(nodos) for i in range(len(nodos))]
	for arista in aristas:
		i,j = arista[0],arista[1]
		i,j = nodos.index(i), nodos.index(j)
		matriz[i][j] += 1
	return matriz


def run_test(nodos,aristas):
	matriz = crear_matriz(nodos,aristas)
	grados = calcular_grados(matriz)
	conexo = grafo_conexo(matriz)
	respuestas = [
	'No es circuito ni camino euleriano',
	'No es circuito ni camino hamiltoniano'
	]
	if conexo:
		respuestas[0] = euler(matriz,grados)
		respuestas[1] = hamilton(grados)
	# print("Euler: {}".format(respuestas[0]))
	# print("Hamilton: {}".format(respuestas[1]))
	return respuestas

 
# nodos = ['A','B','C','D']
# aristas = [
# 	['A','B'],
# 	['B','A'],
# 	['A','C'],
# 	['C','A'],
# 	['B','D'],
# 	['D','B'],
# 	['C','D'],
# 	['D','C']
# ]

# calcular_tipo(nodos,aristas)

newNodes = ["A", "B", "C"]
newEdges = [
	["A", "B"], 
	["A", "C"], 
	["B", "A"],
	["B", "C"],
	["C", "A"],
	["C", "B"]
]

run_test(newNodes, newEdges)

