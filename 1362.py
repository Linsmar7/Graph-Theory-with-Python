from collections import defaultdict 

class Grafo: 
    def __init__(self,grafo): 
        self.grafo = grafo
        self.tamanho = len(grafo)
          
    def bfs(self,s, t, pai): 
        visitado =[False]*(self.tamanho) 
        fila=[] 
        fila.append(s) 
        visitado[s] = True
        while fila: 
            u = fila.pop(0) 
            for ind, val in enumerate(self.grafo[u]): 
                if visitado[ind] == False and val > 0: 
                    fila.append(ind) 
                    visitado[ind] = True
                    pai[ind] = u 
        return True if visitado[t] else False

    def fordFulkerson(self, x, y): 
        pai = [-1]*(self.tamanho) 
        maximo = 0
        while self.bfs(x, y, pai): 
            cami = float("Inf") 
            s = y 
            while s != x: 
                cami = min(cami, self.grafo[pai[s]][s]) 
                s = pai[s] 
            maximo +=  cami 
            v = y 
            while v !=  x: 
                u = pai[v] 
                self.grafo[u][v] -= cami 
                self.grafo[v][u] += cami 
                v = pai[v] 
        return maximo 
  
casos = int(input())

for c in range(casos):
    n, m = list(map(int, input().split()))
    dim = 8+m
    grafo = [[0]*dim for i in range(dim)]
    grafo[0][1:7] = [n//6]*6
    arr = []
    biblioteca = {
        "XS": 1,
        "S": 2,
        "M": 3,
        "L": 4,
        "XL": 5,
        "XXL": 6
    }
    for i in range(m):
        camisas = input().split()
        for j in camisas:
            grafo[biblioteca[j]][7+i] = 1
        grafo[7+i][dim-1] = 1
    g = Grafo(grafo) 
    x, y = 0, dim-1
    maximo = g.fordFulkerson(x, y)
    if maximo == m:
        print("YES")
    else:
        print("NO")