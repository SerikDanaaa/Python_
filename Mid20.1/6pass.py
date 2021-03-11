n = int(input())
while n:
    txt = list(map(str,input().split()))
    cntA = 0
    cnta = 0
    cnto = 0
    for i in txt[0]:
        if i in "QWERTYUIOPASDFGHJKLZXCVBNM":
            cntA += 1
    for i in txt[1]:
        if i.lower() in "aeuio":
            cnta += 1
    for i in txt[2]:
        if i in "1234567890":
            cnto += 1    
    n -= 1
print(cntA)
print(cnta)
print(cnto)                



