UNVISITED = -1

#vetores de inteiro
dfs_num = []
dfs_low = []
s = []
visited = []

#vetor de vetor de inteiro
AdjList = [[] for x in range(100007)]

dfsNumberCounter = 0
numSCC = 0

m = {}

def tarjanSCC(u):
    global dfsNumberCounter
    global dfs_num
    global dfs_low
    global visited
    global numSCC
    dfsNumberCounter += 1
    dfs_num[u] = dfsNumberCounter
    dfs_low[u] = dfs_num[u]
    s.append(u)
    visited[u] = 1;
    for i in range(len(AdjList[u])):
        v = AdjList[u][i]
        if dfs_num[v] == UNVISITED:
            tarjanSCC(v)
        if visited[v]:
            dfs_low[u] = min(dfs_low[u], dfs_low[v])
    if dfs_low[u] == dfs_num[u]:
        tam = 0
        while True:
            tam += 1
            v = s[-1]
            s.pop()
            visited[v] = 0
            if u == v:
                break
        if tam >= 2:
            numSCC += 1
p1 = 0
p2 = 0
vertices = 0
while True:
    try:
        node = input().split()
        if node[0] not in m:
            p1 = vertices
            vertices += 1
            m[node[0]] = vertices
        else:
            p1 = m[node[0]]
        if node[1] not in m:
            p2 = vertices
            vertices += 1
            m[node[1]] = vertices
        else:
            p2 = m[node[1]]
        AdjList[p1].append(p2)
    except EOFError:
        break
dfs_num = [UNVISITED]*vertices
dfs_low = [0]*vertices
visited = [0]*vertices
for i in range(vertices):
    if dfs_num[i] == UNVISITED:
        tarjanSCC(i)
print(numSCC)