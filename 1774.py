class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    def addAresta(self, u, v, w):
        self.grafo.append([u, v, w])

    def procura(self, parent, i):
        if parent[i] == i:
            return i
        return self.procura(parent, parent[i])

    def uniaoConj(self, parent, rank, x, y):
        xroot = self.procura(parent, x)
        yroot = self.procura(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        custoTotal = 0
        i = 0
        e = 0
        self.grafo = sorted(self.grafo, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.grafo[i]
            i = i + 1
            x = self.procura(parent, u)
            y = self.procura(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.uniaoConj(parent, rank, x, y)
        for u, v, custoCabo in result:
            custoTotal = custoTotal + custoCabo
        print(custoTotal)

verticesArestas = input()
verticesArestasArray = verticesArestas.split(' ') #transformação em array de strings
vertices = int(verticesArestasArray[0])
arestas = int(verticesArestasArray[1])
g = Grafo(vertices)
for i in range(arestas):
    aresta = input()
    arestaArray = aresta.split(' ')
    arestaArrayInt = [int(x) for x in arestaArray] #transformação em array de int
    g.addAresta(arestaArrayInt[0]-1, arestaArrayInt[1]-1, arestaArrayInt[2])

g.kruskal()