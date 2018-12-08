def parseData(data):
    aristas = []
    for arista in data['aristas']:
        aristas.append(tuple(arista))