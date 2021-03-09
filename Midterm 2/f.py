aza,dau = map(int,input().split())
cnt = 0
while aza < dau:
    aza *= 3
    dau *= 2
    cnt += 1
if aza > dau:    
    print(cnt)    
else:
    print(cnt+1)