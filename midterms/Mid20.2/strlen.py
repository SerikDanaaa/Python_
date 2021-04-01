def f(n):
    if len(n) % 2 == 1:
        return 1
    else:
        return 0    
txt = list(map(str,input().split()))
ans = list(map(f,txt))
print(ans.count(1))
