def dijkstra(o, d, n):
    cd = 0
    nt = 0
    arrD = [2**25]*(n+1)
    arrV = [False]*(n+1)
    arrD[o] = 0
    for i in range(1, n+1):
        cd = 2**25
        if arrV[d]:
            break
        for j in range(1, n+1):
            if arrD[j] < cd and not arrV[j]:
                cd = arrD[j]
                nt = j
        if cd == 2**25:
            break
        arrV[nt] = True
        for j in range(1, n+1):
            if cd + grafo[nt][j] < arrD[j]:
                arrD[j] = cd + grafo[nt][j]
    return arrD[d]
while True:
    grafo = [[2**25]*501 for i in range(501)]
    r = 0
    ne = [int(x) for x in input().split()]
    n = ne[0]
    e = ne[1]
    if n == 0 and e == 0:
        break
    for i in range(e):
        xyz = [int(x) for x in input().split()]
        x = xyz[0]
        y = xyz[1]
        z = xyz[2]
        grafo[x][y] = z
        if grafo[y][x] != 2**25:
            grafo[x][y] = grafo[y][x] = 0
    k = int(input())
    for i in range(k):
        od = [int(x) for x in input().split()]
        o = od[0]
        d = od[1]
        r = dijkstra(o, d, n)
        if(r == 2**25):
            print("Nao e possivel entregar a carta")
        else:
            print(r)
    print("")