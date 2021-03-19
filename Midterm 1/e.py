n = int(input())
a = {}
while n:
    txt = input().split()
    for i in range(2,2+int(txt[1])):
        a[txt[i]] = txt[0]      
    n -= 1
m = int(input())
while m:
    city = input()
    if city in a:
        print(a[city])
    else:
        print("Unknown")   
    m -= 1         