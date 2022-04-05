valores = [] #array com as entradas
caso = 0 #número do caso atual
while valores != ['0', '0', '0', '0']:
    CELP = input() #input do usuário
    valores = CELP.split(' ')
    if valores == ['0', '0', '0', '0']:
        break
    caso += 1 #aumento do número do caso atual
    #transformar o input em inteiros
    C = int(valores[0])
    E = int(valores[1])
    L = int(valores[2])
    P = int(valores[3])
    arrayCords = [] #array com as tuplas (coordenadas das estradas)
    teste2 = [] #array auxiliar
    teste = [] #array com os valores onde a cidade da familia se liga
    #controladores de while
    i = 0
    j = 0
    while i < E:
        cord = list(input().strip().split(" ")) #entrada das estradas
        deb2 = [float(x) for x in cord] #transformando cada valor em float
        deb3 = [int(x) for x in deb2] #transformando os valores em float em int
        arrayCords.append(deb3) #transformação em array dentro de array
        i += 1
    while j < P:
        for x in arrayCords:
            #verificação de quais cidades estão ligadas por estradas com a cidade da familia
            if L == x[0] or x[0] in teste2:
                teste.append(x[1])
            elif L == x[1] or x[1] in teste2:
                teste.append(x[0])
        teste2 = teste2 + teste
        j += 1
    xyz = list(set(teste)); #remoção de duplicata
    if L in xyz:
        xyz.remove(L) #remoção da cidade da familia
    xyz.sort() #ordenando em ordem crescente
    print("Teste", caso)
    #o URI só aceitou os valores das cidades onde a familia pode ir em formato de uma string só, então eu fiz isso para converter os valores de int para string:
    resultado = ''
    if(len(xyz) > 0):
        for o in range(len(xyz)):
            resultado = resultado + str(xyz[o]) + ' '
    print(resultado + '\n')