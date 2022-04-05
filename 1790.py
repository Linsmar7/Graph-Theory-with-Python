from collections import defaultdict

pontes = 0

class Grafo:
  
    def __init__(self,vertices):
        self.V = vertices
        self.grafo = defaultdict(list)
        self.temp = 0

    def addEdge(self,u,v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def recurssaoProcura(self,u, visitado, pai, menor, achado):
        global pontes
        visitado[u] = True
        achado[u] = self.temp
        menor[u] = self.temp
        self.temp += 1

        for v in self.grafo[u]:
            if visitado[v] == False :
                pai[v] = u
                self.recurssaoProcura(v, visitado, pai, menor, achado)
                menor[u] = min(menor[u], menor[v])
                if menor[v] > achado[u]:
                    pontes = pontes + 1
     
                     
            elif v != pai[u]:
                menor[u] = min(menor[u], achado[v])

    def initPonte(self):
        global pontes
        visitado = [False] * (self.V)
        achado = [float("Inf")] * (self.V)
        menor = [float("Inf")] * (self.V)
        pai = [-1] * (self.V)
        for i in range(self.V):
            if visitado[i] == False:
                self.recurssaoProcura(i, visitado, pai, menor, achado)
        print(pontes)

while(True):
    try:
        cidadesPontes = [int(e)+1 for e in input().split()]
        grafo = Grafo(cidadesPontes[0])
        for i in range(cidadesPontes[1]):
            ponte = [int(e)-1 for e in input().split()]
            grafo.addEdge(ponte[0], ponte[1])
        grafo.initPonte()
    except EOFError:
        break   