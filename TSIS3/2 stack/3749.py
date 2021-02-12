a = list(map(int,input().strip().split()))
b = dict()
cnt = 0
for i in a:
    if i not in b:
        b[i] = 0
        cnt += 1
print(cnt)
        
        
