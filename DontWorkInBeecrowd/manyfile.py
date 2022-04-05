def ordenarTopologica(grafo):
    resultado = []
    graus = [0]*len(grafo) #cria um array do tamanho n (quantidade de vertices) e coloca o valor 0 em tudo
    for vertice in grafo:
        for vizinho in vertice:
            graus[vizinho] += 1 #adiciona 1 pra cada vizinho que o vertice tem
    fila = [v for v in range(len(grafo)) if graus[v] == 0] #cria uma fila
    while fila:
        vertice = fila.pop()
        resultado.append(vertice)
        for vizinho in grafo[vertice]:
            graus[vizinho] -= 1
            if graus[vizinho] == 0:
                fila.append(vizinho)
    return resultado #se o array tiver vazio = ciclico, se não, retorna um array ordenado   

while True:
    try:
        n = int(input())
        grafo = []
        grafoOrdenar = []
        grafoDependencia = {}
        feitos = set() #demorei pra lembrar que set não aceita números iguais
        tempo = 0
        for i in range(n):
            vertice = input().split() #entrada em string
            verticeArrayInt = [int(x) for x in vertice] #transformação em array de int
            grafo.append(verticeArrayInt) #joga dentro de um array
        for j in grafo: #remove o 1° número (a quantidade de dependencias do nó) e diminui em 1 em cada valor de dependencia, já que os arrays começam em 0
            grafoOrdenar.append([x-1 for x in j[1:len(j)]])
        if not ordenarTopologica(grafoOrdenar): #verifica se não é ciclico
            print(-1)
        else:
            for index, item in enumerate(grafoOrdenar):
                if item == []: #se não tiver dependencias, joga o vertice no array de feitos
                    feitos.add(index)
                else:
                    grafoDependencia[index] = item
            while len(feitos) != n: #enquanto não tiver passado por todos os vertices
                flag = 0
                deb = set(feitos)
                for index, item in grafoDependencia.items():
                    if set(grafoDependencia[index]) <= set(deb): #se feitos estiver incluso nas dependencais do vertice
                        feitos.add(index) #adiciona em feitos o vertice
                        flag = 1 #marca como processado
                if flag == 1:
                        tempo += 1 #adiciona no tempo
            print(tempo+1)
    except EOFError:
        break