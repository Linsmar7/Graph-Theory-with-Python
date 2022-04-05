grafo = {}
DEBUG = 1
casamentos = 0
flag = 0
visitados = set()
while True:
    try:
        node = input().split()
        grafo[node[0]] = node[1]
    except EOFError:
        break
for x in grafo:
    if flag == 1:
        break
    componente = set()
    if x not in visitados:
        componente.add(x)
        visitados.add(x)
        y = grafo[x]
        while True:
            if y in visitados:
                break
            if grafo[y] in componente:
                visitados.add(y)
                casamentos += 1
                break
            elif len(visitados)+DEBUG != len(grafo):
                componente.add(y)
                visitados.add(y)
                y = grafo[y]
            else:
                flag = 1
                break
print(casamentos)