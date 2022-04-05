def bipartido(x):#passa o array/dicionario grupos
	cor = [None]*len(x) #cria um array do tamanho do array grupos com None em cada elemento
	for i in range(len(x)):
		if not cor[i]: #se não existir (none)
			queue = [i] #cria um array/fila com o elemento atual
			cor[i] = 'preto' #"pinta" o elemento atual de preto
			while len(queue) > 0: #enquanto existir a fila
				u = queue.pop(0) #passa o primeiro da fila pra u
				for v in x[u]: #pra cada elemento no array do indice u em dicionario grupos
					if cor[v] ==  cor[u]:
						return 0
					if not cor[v]:
						queue.append(v)
						cor[v] = 'preto' if cor[u] == 'branco' else 'branco' #se a cor do 'u' (pop da fila) for branca, pinta o nó atual do for de preto, se não, pinta de branco
	return 1


n = int(input()) #quantidade de orcas
i = 0
#aqui eu transformo a entrada em um array com arrays dentro com a relação de não comunicação entre as orcas, por exemplo:
#[[1, 2, 3], [0, 4], [0, 3], [0, 2, 4], [1, 3]] -> [1, 2, 3] está na posição 0 do array maior, ou seja, a orca 0 não se comunica com a orca 1, 2 e a 3 e assim por diante
grupos = {}
while i < n:
    orca = input() #entrada em string
    orcaArray = orca.split(' ') #transformação em array de strings
    orcaArratInt = [int(x) for x in orcaArray] #transformação em array de int
    resultado = [] #array menor para colocar as orcas que se comunicam com a orca atual
    j = 0
    while j < len(orcaArratInt):
        if j != i and orcaArratInt[j] == 0: #verificando a comunicação entre elas
            resultado.append(j) #cria-se o array menor
        j += 1
    grupos[i] = resultado #joga o array menor em um dicionario
    i += 1
if n < 3:
    print("Bazinga!")
elif bipartido(grupos):
    print("Bazinga!")
else:
    print("Fail!")