def ordenarTopologica(grafo):
    resultado = []
    graus = [0]*len(grafo) #cria um array do tamanho n (quantidade de vertices) e coloca o valor 0 em tudo
    for index, item in grafo.items():
        for index, item in enumerate(item):
            graus[item] += 1 #adiciona 1 pra cada vizinho que o vertice tem
    fila = [v for v in range(len(grafo))] #cria uma fila
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
        grafoOrdenar = {}
        grafoDependencia = {}
        feitos = set() #demorei pra lembrar que set não aceita números iguais
        tempo = 0
        for i in range(n):
            vertice = input().split() #entrada em string
            if vertice == "0":
                feitos.add(i)
            else:
                for j in range(int(vertice[0])):
                    grafoDependencia[i+1].append(int(vertice[j+1]))
        for i in range(n):
            for j in grafoDependencia[i]:
                grafoOrdenar[j].append(i)
        if not ordenarTopologica(grafoDependencia):
            print(-1)
        else:
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