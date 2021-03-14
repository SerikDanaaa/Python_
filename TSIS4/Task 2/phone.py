import re
n = int(input())
while n:
    txt = input()
    pattern = r'^[7-9]\d{9}\b'
    ans = re.search(pattern,txt)
    if ans:
        print("YES")
    else:
        print("NO")    
    n -= 1

