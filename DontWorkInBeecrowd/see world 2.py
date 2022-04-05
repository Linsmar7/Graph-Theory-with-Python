def isBipartite(x):
    grupos = {}
    for orca in range(len(x)):
        if orca not in grupos:
            vizinhos = [orca]
            proximos = []
            grupoAtual = True
            while vizinhos:
                out = vizinhos.pop(0)
                if out in grupos:
                    if grupos[out] != grupoAtual:
                        return False
                else:
                    grupos[out] = grupoAtual
                    for i in x[out]:
                        proximos.append(i)
                if vizinhos == []:
                    grupoAtual = not grupoAtual
                    vizinhos, proximos = proximos,vizinhos
    return True


n = int(input()) #quantidade de orcas
i = 0
#aqui eu transformo a entrada em um array com arrays dentro com a relação de não comunicação entre as orcas, por exemplo:
#[[1, 2, 3], [0, 4], [0, 3], [0, 2, 4], [1, 3]] -> [1, 2, 3] está na posição 0 do array maior, ou seja, a orca 0 não se comunica com a orca 1, 2 e a 3 e assim por diante
grupos = []
while i < n:
    orca = input() #entrada em string
    orcaArray = orca.split(' ') #transformação em array de strings
    orcaArratInt = [int(x) for x in orcaArray] #transformação em array de int
    resultado = [] #array menor para colocar as orcas que se comunicam com a orca atual
    j = 0
    while j < len(orcaArratInt):
        if j != i and orcaArratInt[j] == 1: #verificando a comunicação entre elas
            resultado.append(j) #cria-se o array menor
        j += 1
    grupos.append(resultado) #joga o array menor no maior
    i += 1
if n < 3:
    print("Bazinga!")
elif isBipartite(grupos):
    print("Bazinga!")
else:
    print("Fail!")