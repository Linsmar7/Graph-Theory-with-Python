def bipartido(x):
    visitado = [False] * len(x)
    grupo = [-1] * len(x)
    def dfs(v, c):
        visitado[v] = True
        grupo[v] = c
        for u in x[v]:
            if not visitado[u]:
                dfs(u, 1 - c)
    for i in range(len(x)):
        if not visitado[i]:
            dfs(i, 0)
    for i in range(len(x)):
        for j in x[i]:
            if grupo[i] == grupo[j]:
                return False
    return True


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