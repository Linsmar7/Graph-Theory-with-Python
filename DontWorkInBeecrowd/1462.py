#NÃO PASSA NO URI (TLE) GALLAI EM TEMPO n^2
def check(arr, n):
    for x in arr:
        if n < x:
            return True 
    return False

def graus(arr):
    return all( x>=y for x, y in zip(arr, arr[1:]))
    
def gallai(arr):
    if sum(arr) % 2: # if 0 = par, 0 == False
        return False
    if graus(arr):
        for k in range(1, len(arr) + 1):
            esquerda = sum(arr[:k])
            direita =  k * (k-1) + sum([min(x,k) for x in arr[k:]])
            if esquerda > direita:
                return False
    else:
        return False
    return True

while True:
  try:
    n = int(input())
    listaInicial = [int(x) for x in input().split()]
    listaInicial.sort(reverse=True)
    if check(listaInicial, n):
        print("impossivel")
    elif gallai(listaInicial):
        print("possivel")
    else:
        print("impossivel")
  except EOFError:
    break