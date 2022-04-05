def resultado(graph):
    #Nos que ja foram vistiados
    visited = set()
    count = 0
    #Percorre os elementos do grafo
    for node1 in graph:
        #Faz um set para os elementos do ciclo atual
        atual = set()
        #Se o no nao foi visitado
        if node1 not in visited:
            visited.add(node1)
            #Adiciona ele na lista do ciclo atual
            atual.add(node1)
            #Pega o no que ele aponta
            node2 = graph[node1][0]
            while True:
                #Se o no apontado nao foi visitado
                if node2 not in visited:
                    #Testa se quem ele aponta ja esta na lista atual
                    if graph[node2][0] in atual:
                        #Se estiver, adiciona nos visitados temporarios
                        visited.add(node2)
                        #Soma mais um no contador
                        count += 1
                        break
                    #Se nao esta na lista atual e ainda tiver nos
                    elif len(graph) != len(visited)+1:
                        #Adiciona nos visitados temporario
                        visited.add(node2)
                        #Adiciona na lista de atual
                        atual.add(node2)
                        #E pega o no que ele aponta
                        node2 = graph[node2][0]
                    #Se nao tiver mais nos, retorna o contador
                    else:
                        return count
                #Caso ja tenha sido visitado, nao fecha o ciclo
                else:
                    break
    return count
                        
graph = {}   
while(True):
    try:
        a, b = map(str,input().split())
        graph[a] = []
        graph[a].append(b)
    except EOFError:
        break
print(resultado(graph))