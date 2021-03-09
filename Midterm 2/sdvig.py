l = input().split()
k = int(input())

cd = k % len(l)
for i in range(cd,len(l)):
    print(l[i], end = ' ')
for i in range(cd):
    print(l[i], end = ' ')    