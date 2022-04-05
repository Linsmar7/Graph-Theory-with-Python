visitados = [False]*1000
cont = 0
def bfs(x):
    f = []
    visitados[x] = True
    f.append(x)
    while f:
        a = f[0]
        f.pop(0)
        for i in range(len(g[a])):
            if not visitados[g[a][i]]:
                visitados[g[a][i]] = True
                f.append(g[a][i])
casos = int(input())
for i in range(1, casos+1):
    bla = [int(x) for x in input().split()]
    if len(bla) > 1:
        vertices = bla[0]
        arestas = bla[1]
    else:
        vertices = bla[0]
        arestas = int(input())
    g = [[] for o in range(vertices+1)]
    for j in range(arestas):
        xy = [int(x) for x in input().split()]
        verticeX = xy[0]
        verticeY = xy[1]
        g[verticeX].append(verticeY)
        g[verticeY].append(verticeX)
    cont = 0
    visitados = [False]*1000
    bfs(1)
    for j in range(1, vertices+1):
        if not visitados[j]:
            bfs(j)
            cont = cont+1
    if cont == 0:
        print("Caso #" + str(i) + ": a promessa foi cumprida")
    else:
        print("Caso #" + str(i) + ": ainda falta(m) " + str(cont) + " estrada(s)")