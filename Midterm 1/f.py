n = int(input()) 
s, t = input(), ''
for i in s:
    if ord(i) + n <= 90:
        t += chr(ord(i) + n)
    else:
        t += chr(ord(i) + n - 26)
print(t)