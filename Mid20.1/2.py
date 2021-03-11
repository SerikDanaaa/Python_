f = open("input.txt","r")
f1 = open("output.txt","w")
txt = list(map(str,f.read().split()))
ok = True
for i in range(1,len(txt)):
    if len(txt[i-1]) > len(txt[i]):
        ok = False
        break

if ok:
    print("Yes",f1.write("Yes"))
else:
    print("No", f1.write("No"))

