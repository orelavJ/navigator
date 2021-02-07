#nodos = ["start", 'prt004', 'prt005', "prtf04", "prt001", "prtf001", "prtf15"]
#inicio = prontera(156, 80)
import ast, math, sys
in_text = ""

texto = open("diccionario_mapas_RO.txt", 'r')
contenido = texto.read()
diccionario = ast.literal_eval(contenido)

distancias = diccionario
nodos = [node for node, value in distancias.items()]

adyacentes_origen = sys.argv[1]
xy_origen = sys.argv[2]
target = sys.argv[3].split(',')

#print("Origen:", adyacentes_origen)
#print("Coordenada X:", sys.argv[2].split(' ')[0], "Coordenada Y:", sys.argv[2].split(' ')[1])
#print("Nodos destino:", target)
count = 0
adyacentes_origen = adyacentes_origen.split(',')

xy_origen = xy_origen.split(' ')
distancias["start"] = {}
#print(distancias)

for nodo in adyacentes_origen:
    distancias["start"][nodo] = xy_origen[count]
    for k, v in distancias.items():
        if nodo == k:
            v["start"] = xy_origen[count]
            count = count+1


candidatos = {'start':0}
distancias_minimas = {nodo:{"min":None, "vertice":None} for nodo in nodos}

distancias_minimas["start"]["min"] = 0
distancias_minimas["start"]["vertice"] = "start"
visitados = []
punto_actual = "start"


while True: 

    distancia_actual = distancias_minimas[punto_actual]["min"]
    for adyacente, peso in distancias[punto_actual].items():
   
        if punto_actual in visitados:
            continue
        candidatos[adyacente] = int(peso)

        #print(type(distancia_actual), type(peso))
        nuevaDistancia = distancia_actual + int(peso)

        #print(punto_actual)

        if distancias_minimas[adyacente]["min"] is None or nuevaDistancia < distancias_minimas[adyacente]["min"]:
            distancias_minimas[adyacente]["min"] = nuevaDistancia
            distancias_minimas[adyacente]["vertice"] = punto_actual

    visitados.append(punto_actual)

    del candidatos[punto_actual]

    if not candidatos:
        break
    punto_actual = sorted(candidatos.items(), key = lambda x: int(x[1]))[0][0]

#print(distancias["prt001"])
#target = ["prtf12-1", "prtf11-1", "prtf14", "prtf15"]

source = "start"
camino = []
#while True:
#    for k, v in distancias_minimas.items():
#        if k == target:
#            camino.append(v["vertice"])
#            target = v["vertice"]
#    if camino[-1] == source:
#        break
#print(camino)
dist_min = 99999
ult_map = ""
#print(distancias["start"])
for node, v in distancias_minimas.items():
    if node in target and v["min"] != None and v["min"]<dist_min:
        #print(node, v) 
        ult_map = node
        #print(ult_map)
        dist_min = v["min"]

objetivo=ult_map
#print(ult_map)
#print(distancias_minimas["gef009"])
#print(ult_map, dist_min)
pasos = 0
#print(diccionario["mocf001"])
#print(diccionario["mocf13-1"])
#print(diccionario["moc003"])
#print(distancias_minimas["mocf001"])
while True:
    for k, v in distancias_minimas.items():
        if k == ult_map:
            #print(k)
            #print(ult_map)
            camino.append(v["vertice"])
            pasos += v["min"]
            #print(pasos)
            ult_map = v["vertice"]
    if camino[-1] == "start":
        break

#print(distancias_minimas)
camino.insert(0,objetivo)
pasos = distancias_minimas[objetivo]["min"]
print(distancias_minimas["prtf14"])
print(camino, pasos)

