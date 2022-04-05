class Grafo:

    def __init__(self, v, a):
        self.v = v
        self.a = a
        self.rota = [[0]*501 for i in range(501)]
        
        
def dijkstra(o, d):
    db = 0
    st = [None]*501
    mom = [-1]*501
    cst = [1000000]*501
    st[o] = o
    cst[o] = 0
    while True:
        mincst = 999999
        for i in range(grafo.v):
            if mom[i] == -1 and mincst > cst[i]:
                mincst = cst[db]
                db = i
        if mincst == 999999:
            break
        mom[db] = st[db]
        for i in range(grafo.v):
            if cst[i] > cst[db] + grafo.rota[db][i]:
                cst[i] = cst[db] + grafo.rota[db][i]
                st[i] = db
    if cst[d] < 999999:
        print(cst[d])
    else:
        print("Nao e possivel entregar a carta")
while True:
    ne = [int(x) for x in input().split()]
    n = ne[0]
    e = ne[1]
    if n == 0 and e == 0:
        break
    grafo = Grafo(n+1, e)
    for i in range(n+1):
        for j in range(n+1):
            grafo.rota[i][j] = 999999
    for i in range(e):
        xyz = [int(x) for x in input().split()]
        x = xyz[0]
        y = xyz[1]
        z = xyz[2]
        if grafo.rota[y][x] != 999999:
            grafo.rota[x][y] = 0
            grafo.rota[y][x] = 0
        else:
            grafo.rota[x][y] = z
    k = int(input())
    for i in range(k):
        od = [int(x) for x in input().split()]
        o = od[0]
        d = od[1]
        dijkstra(o, d)
    print("\n")