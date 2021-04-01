n = int(input())
txt = input()
t = str()
for i in txt:
    if ord(i) + n <= 90:
        t += chr(ord(i) + n)
    else:
        t+= chr(ord(i) + n - 26)
print(t)
