a = [1,2,3,4,5,6,7,8]
n = int(input())
b = []
for i in a[:n]:
    b.append(i)

for j in a[len(a)-n:]:
    b.append(j)
    
print(b)