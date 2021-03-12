import re
n = int(input())
while n > 0:
    s = ''
    s = str(input())
    pattern = r"^([+-])?\d*\.+\d+$"

    x = re.findall(pattern, s)
    if x:
        print(True)
    else:
        print(False)
    n -= 1