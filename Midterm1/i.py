n =int(input())
list1 = list(map(str,input().split()))
k = int(input())

x = ""
y = ""
for i in list1[0:k]:
    x += i
for i in list1[k:]:
    y += i

print(x*y)