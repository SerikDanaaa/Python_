n, x = input(), input()
xlist, ans = [], []

for i in range(len(n)):
    if n[i] == x:
        xlist.append(i)

for i in range(len(n)):
    minv = len(n)
    #2101232101
    #kbtupoints
    #0123456789
    #t -> in places 2, 8
    for j in xlist:
        if abs(i - j) < minv:
            minv = abs(i - j)
    ans.append(minv)
print(ans)