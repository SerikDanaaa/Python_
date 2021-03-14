n = int(input())
a = tuple(map(int,input().split()))
b = tuple(map(int,input().split()))
c = tuple(map(int,input().split()))
zipplist = tuple(zip(a,b,c))
y = tuple()
sum = 0
for i in range(0,len(zipplist)):
    sum = 0
    x = zipplist[i]
    for j in x:
        sum += j
    y1 = list(y)
    y1.append(sum)
    y = tuple(y1)

print(y)