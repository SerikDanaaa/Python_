n = int(input())
while n:
    txt = input().split()
    for i in txt:
        ok = False
        a = list()
        for j in i:
            if j in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOOPASDFGHJKLZXCVBNM":
                a.append(j)
        for k in range(100):
            if len(a) == 2**k:
                ok = True
        if ok:
            print("N", end=" ")
        else:
            print("C",end=" ")  
    print()   
    n -= 1    




