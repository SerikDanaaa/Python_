a = list(map(int,input().split()))
b = list(map(int,input().split()))

ok = False
k = int(input())
res = list(zip(a,b))

for i in range(0,len(res)):
    a = res[i]
    a1 = a[0]
    a2 = a[1] 

    for j in range(a1,a2+1):
        if j == k:
            ok = True
            break
    if ok:
        print(res[i])
        ok = False

