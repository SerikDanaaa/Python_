import re
txt = input()
t = input()
s = input()
f = input()
txt1 = txt.replace(t,s)

x = re.findall(f,txt1)
print(len(x))