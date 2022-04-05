duplaCamisetas = [[0]*2]*40
arr = [0]*10
ok = False
x = 0

def trab(p):
    global ok
    global x
    global duplaCamisetas
    global arr
    if p == x+1:
        ok = True
        return
    if ok:
        return
    if arr[duplaCamisetas[p][0]] != 0:
        arr[duplaCamisetas[p][0]] -= 1
        trab(p+1)
        arr[duplaCamisetas[p][0]] += 1
    if arr[duplaCamisetas[p][1]] != 0:
        arr[duplaCamisetas[p][1]] -= 1
        trab(p+1)
        arr[duplaCamisetas[p][1]] += 1
def switch(s):
    if s == "XS":
        return 1
    if s == "S":
        return 2
    if s == "M":
        return 3
    if s == "L":
        return 4
    if s == "XL":
        return 5
    if s == "XXL":
        return 6
cases = int(input())

for i in range(cases):
    de = [int(e) for e in input().split()]
    n = de[0]
    x = de[1]
    for j in range(10):
        arr[j] = n/6
    for k in range(1, x+1):
        es = input().split()
        s1 = es[0]
        s2 = es[1]
        duplaCamisetas[k][0] = switch(s1)
        duplaCamisetas[k][1] = switch(s2)
    ok = False
    trab(1)
    if ok:
        print("YES")
    else:
        print("NO")