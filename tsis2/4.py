gain = list(map(int,input().strip().split()))

alt=0
mx=0
for i in gain:
    alt+=i
    if (alt>mx):
        mx = alt
print(mx)   
        