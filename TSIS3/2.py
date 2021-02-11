a = list(map(int,input().strip().split()))
mn = 1001
for i in range(0,len(a)):
    if  (mn > a[i] and a[i] > 0):
        mn = a[i]
print(mn)        

