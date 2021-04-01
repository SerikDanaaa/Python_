a = list(map(int,input().split()))
b = list(map(int,input().split()))
k = int(input())
c = zip(a,b)
cnt = 0
for i in c:
    a = i
    for j in range(a[0],a[1]):
        if j == k:
            cnt += 1
print(cnt)            