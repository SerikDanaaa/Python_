n = int(input())
a = {}
list1 = list()
while n:
    txt = input().split()
    name = txt[0]
    for i in range(1,len(txt)):
        if not txt[i] in a.values():
            list1.append(txt[i])
    
    a.update({name : list1})
    n -= 1
for i in a:
    print(i,*a[i])        