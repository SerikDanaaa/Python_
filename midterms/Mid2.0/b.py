with open('input.txt','r') as f:
    a = f.readlines()
ok = True
with open('output.txt','w') as f1:
    for i in range(1,len(a)):
        if a[i] < a[i-1]:
            ok = False
    if ok:
        print("YES")
        f1.write("YES")
    else:
        print("NO")
        f1.write("NO")
    for i in range(len(a)):
        print(a[i])    


