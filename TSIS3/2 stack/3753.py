a,b = map(int,input().split())
s1 = set()
s2 = set()
for i in range(a):
    s1.add(int(input()))
for i in range(b):
    s2.add(int(input()))
print(len(s1&s2))
print(*sorted(s1&s2))   

print(len(s1-s2))
print(*sorted(s1-s2))

print(len(s2-s1))
print(*sorted(s2-s1))

