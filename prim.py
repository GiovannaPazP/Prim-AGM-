#---------------------------------------------------------------#
#                 Implementação Algoritmo de Prim               #
#                           Giovanna Paz                        #
#                   Ciência da Computação - UFSJ                #
#---------------------------------------------------------------#

import igraph as ig
import matplotlib.pyplot as plt
import sys
import random

g = ig.Graph.Read_Ncol("exemplo_prim.ncol", weights='if_present', directed=False)

#Variaveis
nVertices = 0
vr = 0
prox_v = 0
abertos = []
vizinhos = []
arestas = []
solucao = []
peso = sys.maxsize

#Inicializa
nVertices = g.vcount()
n_random = random.randrange(0, nVertices)
vr = g.vs[n_random]

#grafo de saída
gs = ig.Graph(nVertices)

letra=65
for i in g.vs:
    gs.vs[i.index]["name"]=chr(letra+i.index)
    abertos.append(i.index)

print(g)

#algoritmo
while abertos:

    abertos.remove(vr.index)
    solucao.append(vr.index)

    vizinhos = g.neighbors(vr.index)
   
    for v in vizinhos:
        if peso > g.es.select(_source=vr.index, _target=v)["weight"][0]:
            peso = g.es.select(_source=vr.index, _target=v)["weight"][0]
            prox_v = v

    #get_eid==-1 quando a aresta não existe no grafo
    if gs.get_eid(vr.index, prox_v, directed=False, error=False)==-1:
        arestas+=[{vr.index, prox_v}]
        gs.add_edges([(vr.index, prox_v)])
        gs.es.select(_source=vr.index, _target=prox_v)["weight"]=peso

    peso = sys.maxsize

    aux = set(abertos).intersection(set([prox_v]))
    if aux==set():
        if abertos:
            vr = g.vs[abertos[0]]
        else:
            vr = 0
    else:
        vr = g.vs[prox_v]


print("solucao: ", set(solucao))
print("arestas: ", arestas)


fig, ax = plt.subplots()
ig.plot(
    gs,
    target=ax,
    layout='circle',
    vertex_color='steelblue',
    vertex_label=gs.vs['name'],
    edge_label=gs.es['weight'],
    edge_color='#222',
    edge_align_label=True,
    edge_background='white'
)
plt.show()