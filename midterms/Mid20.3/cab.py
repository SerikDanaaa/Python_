a,b = map(int,input().split())
taken = list(map(int,input().split()))
nottaken = list()
for i in range(a,b+1):
    if i not in taken:
        nottaken.append(i)
print(*nottaken)            

