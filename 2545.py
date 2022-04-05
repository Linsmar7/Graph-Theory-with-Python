#Ordenação Topológica
def topologicalSort(graph2, N):
    #Cria um vetor para guardar as dependencias zerados de todos os vértices.
    in_degree = [0]*(N)
         
    #Percorre listas de adjacências para incrementar as dependencias
    for i in graph2:
        for j in graph2[i]:
            in_degree[j-1] += 1

    #Cria uma fila e enfileira todos os vértices com 0 dependencias
    queue = []
    for i in range(N):
        if in_degree[i] == 0:
            queue.append(i)
 
    #Contador de vertices visitados
    cnt = 0
 
    #Cria um vetor para guardar o resultado da ordenação
    top_order = []
 
    #Desenfileira os vertices e enfileira seus adjacentes quando esses
    #ficam com 0 dependencias
    while queue:
        
        #Desenfileira o topo da pilha e adiciona na ordenação
        u = queue.pop(0)
        top_order.append(u)
 
        #Diminui em 1 a dependencia dos vizinhos do nó 
        #retirado da fila e adicionado na ordernação 
        for i in graph2[u+1]:
            in_degree[i-1] -= 1
            #Se o vizinho ficar com 0 dependencias, adiciona na fila
            if in_degree[i-1] == 0:
                queue.append(i-1)
                
        #Aumenta em 1 o contador de vertices visitados
        cnt += 1

    #Testa se o grafo é ciclico
    if cnt != N:
        #print("There exists a cycle in the graph")
        return False
    else :
        #print(top_order)
        return True

#Função para imprimir o resultado
def resultado(graph1, executados, N):
    #Começa em 1 por causa dos vértices sem dependencias
    count = 1
    #Repete até todos os vértices serem executados
    while len(executados) != N:
        exec = executados.copy()
        #Variavel de controle para saber se algum nó foi executado
        aux = False
        #Percorre cada nó do grafo
        for g in graph1:
            #Se as dependencias dele estiverem todas executadas
            if(set(graph1[g]).issubset(exec)):
               #Adiciona ele na lista de executados
               executados.add(g)
               aux = True
        #Após percorrer todos os nós, caso algum tenha sido executado
        if aux:
               #Aumenta em 1 o contador
               count += 1
    #Retorna o tempo demandado
    return count
    
while(True):
    try:
        #Recebe a quantidade de nós
        N = int(input())
        #Grafo que guarda as dependencias de cada nó
        graph1 = {}
        #Grafo que guarda os adjacentes de cada nó
        graph2 = {}
        #Set com os nós já executados
        executados = set()
        #Percorre a quantidade de vértices, preenchendo o grafo 1
        for i in range(N):
            #Inicializa o grafo 1
            graph1[i+1] = []
            #Inicializa o grafo 2
            graph2[i+1] = []    
            #Recebe a entrada
            entrada = input().split()
            #Se a entrada for igual a 0, não tem dependencia
            if entrada[0] == "0":
                #Então o nó já pode ser executado
                executados.add(i+1)
            #Caso tem alguma dependencia
            else:
                #Adiciona as dependencias no grafo 1
                for j in range(int(entrada[0])):
                    graph1[i+1].append(int(entrada[j+1]))
        #Percorre os nós novamente
        for i in range(N):
            #Adiciona os nós adjecentes no grafo 2
            for j in graph1[i+1]:
                graph2[j].append(i+1)
        #Se o grafo não for ciclico
        if(topologicalSort(graph2, N)):
            #Imprime a quantidade de tempo
            print(resultado(graph1, executados, N))
        #Se for
        else:
            #Imprime -1
            print(-1)
    except EOFError:
        break   

    
    
            
