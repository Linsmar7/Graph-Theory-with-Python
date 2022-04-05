__authors__ = ''
__group__ = 'Caju'
__id__ = ''
# -*- coding: utf-8 -*-
#Criando a classe nó da árvore
class Node:
    def __init__(self, data):
        self.esquerda = None #lado esquerdo da árvore, onde fica os números menores que a raiz
        self.direita = None #lado direito, onde fica os números maiores
        self.data = data
            
def PreOrder(root, c): #função para a pre-order
    if root is None: #se a raiz não existir, não tem como ordenar
        return

    resultado = [] #array auxiliar para ordenar na ordem raiz->esquerda->direita
    valores = [] #array final
    resultado.append(root) #é colocado a raiz primeiro, seguindo a ordem

    while(len(resultado) > 0): #enquanto existir elementos dentro do array resultado, é feito o while
        shi = resultado.pop() #retira o nó adicionado por último no array resultado e coloca na variável shi
        valores.append(shi.data) #coloca o valor do nó de shi no array valores
        if shi.direita is not None: #se existir um nó a direita, é colocado primeiro no array
            resultado.append(shi.direita)
        if shi.esquerda is not None: #se existir um nó a esquerda, é colocado depois do da direita
            resultado.append(shi.esquerda)
        #fazendo assim, é colocado a raiz no array, depois os da direita, depois o da esquerda, como é sempre retirado o último adicionado pra por no array, fica na pre-order (já que a raiz é retirada logo no inicio da função)
    return valores
    
def PosOrder(root): #função para pos-order
    if root is None:
        return       
    #cria-se 2 arrays e 1 array final
    s1 = []
    s2 = []
    valores = []
    s1.append(root) #coloca a raíz no primeiro array
    while s1:
        #tira o nó de s1 e coloca em s2
        node = s1.pop() 
        s2.append(node)
        #joga os nós da direita e da esquerda do nó atual para o array s1
        if node.esquerda:
            s1.append(node.esquerda)
        if node.direita:
            s1.append(node.direita)
        #depois dos elementos ficarem em ordem ""contrária"" da pos-order em s2, é usado o pop (retirar o último do array) e colocado o valor no array valores
    while s2:
        node = s2.pop()
        valores.append(node.data)
    return valores
    
def InOrder(root): #função para inorder
    shi = root #salva a raiz da árvore
    s1 = []
    valores = []
    while True:
        if shi is not None: #se shi existe, joga no array s1 e atualiza shi para ser o nó a esquerda do nó atual
            s1.append(shi)
            shi = shi.esquerda
        elif(s1): #se shi não existe e s1 existe (foi pro último nó da esquerda)
            #joga todos os valores para o array valores enquanto vai voltando a árvore até a raiz e passando os da direita logo depois
            shi = s1.pop()
            valores.append(shi.data) 
            shi = shi.direita
        else:
            break
    return valores
        
def insert(root, data): #função de inserção
    raiz = Node(data); #primeira raiz da árvore
    x = root; #ponteiro para procurar onde será colocado o novo elemento
    y = None; #ponteiro auxiliar
    while x != None:
        y = x;
        if data < x.data:
            x = x.esquerda;
        else:
            x = x.direita;
    if y == None: #se a árvore está vazia, o elemento sendo adicionado vira a nova raiz
        y = raiz;
    elif data < y.data: #se o elemento for menor que a raiz, vai pra esquerda
        y.esquerda = raiz;
    else: #se o elemento for maior que a raiz, vai para a direita
        y.direita = raiz;
    return y;
    
C = int(input()); #número de casos
i = 0;
while i < C:
    N = int(input()); #quantidade de elementos da árvore do caso atual
    arr = input() #elementos da árvore do caso atual
    lista = list(map(int,arr.split(' '))) #formatação em lista dos elementos
    root = None;
    root = insert(root, lista[0]) #adiciona o primeiro elemento a raiz principal da árvore
    x = 1
    while x < N:
        insert(root, lista[x]) #insere o resto dos elementos a árvore
        x += 1;
    posOrderArray = PosOrder(root)
    preOrderArray = PreOrder(root, N)
    inOrderArray = InOrder(root)
    print("Case", str(i+1) + ":")
    print("Pre.:", *list(preOrderArray), sep=' ')
    print("In..:", *list(inOrderArray), sep=' ')
    print("Post:", *list(posOrderArray), sep=' ')
    print()
    i += 1