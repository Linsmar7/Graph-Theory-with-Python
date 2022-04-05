from collections import defaultdict

BRANCO = 0
CINZA = 1
PRETO = 2
casamentos = 0

nos = []

while True:
    try:
        node = input().split()
        nos.append(node)
    except EOFError:
        break

ENTER = 0
EXIT = 1

end = 0

def grafoDict(a):
    graph = defaultdict(list)
    
    for x, y in a:
        graph[x].append(y)
    return graph

def dfs(graph, start):
    global casamentos
    global end
    state = {v: BRANCO for v in graph}
    stack = [(ENTER, start)]

    while stack:
        act, v = stack.pop()

        if act == EXIT:
            end = 0
            graph.pop(v)
            state[v] = PRETO
        else:
            end = 1
            state[v] = CINZA
            stack.append((EXIT, v))
            for n in graph[v]:
                if not graph[n]:
                    break
                if state[n] == CINZA:
                    casamentos += 1
                elif state[n] == BRANCO:
                    stack.append((ENTER, n))

graph = grafoDict(nos)
while graph and end == 0:
    dfs(graph, next(iter(graph)))
print(casamentos)