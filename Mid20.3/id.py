a = {}
mx = -1
txt = input().split()
for i in txt:
    if i not in a:
        a[i] = 1
    else:
        a[i] += 1
    if a[i] > mx:
        mx = int(i)
print(mx)
    