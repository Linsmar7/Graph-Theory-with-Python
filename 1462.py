#PASSA NO URI GALLAI EM TEMPO LINEAR
def check(arr, n):
    for x in arr:
        if n < x:
            return True 
    return False
    
def gallai(arr, n): #COM TEMPO LINEAR POG
    h = [0]*n
    for i in range(n):
        h[i] = h[i-1] + arr[i]
    if h[n-1] % 2:
        return False
    w = n
    for i in range(1, n):
        while w > 0 and arr[w-1] < i:
            w = w - 1
        y = max(i, w)
        if h[i-1] > (i*(y-1) + h[n-1] - h[y-1]):
            return False
    return True

while True:
  try:
    n = int(input())
    listaInicial = [int(x) for x in input().split()]
    listaInicial.sort(reverse=True)
    if check(listaInicial, n):
        print("impossivel")
    elif gallai(listaInicial, n):
        print("possivel")
    else:
        print("impossivel")
  except EOFError:
    break