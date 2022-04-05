#NÃO PASSA NO URI (TLE)
while True:
  try:
    n = int(input())
    listaInicial = [int(x) for x in input().split()]
    listaInicial.sort(reverse=True)
    amigos = []
    while len(listaInicial) != 0:
        pessoa = listaInicial[0]
        count = 0
        while pessoa > 0 and len(amigos) != 0 and count < len(amigos):
            pessoa -= 1
            if (amigos[count] == 1):
                amigos.pop(count)
            else: 
                amigos[count] -= 1
                count += 1
        if (pessoa > 0):
            amigos.append(pessoa)
        listaInicial.pop(0)
    print ("possivel" if len(amigos) == 0 else "impossivel")
  except EOFError:
    break