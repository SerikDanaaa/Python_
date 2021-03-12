f = open("input.txt","r")
f1 = open("output.txt","w")
txt = list(map(str,f.read().split()))
ok = True
for i in range(1,len(txt)):
    if len(txt[i-1]) > len(txt[i]):
        ok = False
        break
if ok:
    f1.write("Yes")
    print("Yes")
else:
    f1.write("No")
    print("No")

