tabela = [[0]*80]*80 #tabela 50x50 iniciada
passados = [0]*80 #array 50 valores iniciados
total = 0 #resultado

#função pra contar as arestas
def procuraEConta(a, b):
    global total
    i = 0
    passados[a] = 1 #adiciona o vertice atual no array de passados
    while i < b:
        #verifica se existe correlação e se ja foi contado a aresta
        if tabela[a][i] == 1 and passados[i] == 0: 
            #se existe correlação e ainda não foi contado, adiciona 1 e faz a recursão
            total += 1
            procuraEConta(i, b)
        i += 1
T = int(input()) #número de casos
j = 0
while j < T:
    total = 0 #resetando o total pra cada caso
    N = int(input()) #vertice inicial
    
    #quantidade de vertices e arestas
    VA = input()
    valores = VA.split(' ')
    V = int(valores[0])
    A = int(valores[1])
    
    k = 0
    while k < A:
        #arestas
        XY = input()
        valores2 = XY.split(' ')
        X = int(valores2[0])
        Y = int(valores2[1])
        
        #se b está ligado com a, então a está ligado com b, = não tem correlação, 1 = tem
        tabela[X][Y] = 1
        tabela[Y][X] = 1
        k += 1
    procuraEConta(N, V)
    
    #só está sendo contado 1x a aresta (A -> B), então multiplica por 2 pra contar a ida e a volta (A -> B, B -> A)
    total = total*2
    print(total)
    tabela = [[0]*80]*80 #zerar tabela
    passados = [0]*80 #zerar array
    j += 1