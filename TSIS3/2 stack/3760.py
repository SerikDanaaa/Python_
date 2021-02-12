n = int(input())
a = dict()
for i in range(n):
    b,c = input().split()
    a[b] = c
    a[c] = b
d = input()
print(a[d])    
    