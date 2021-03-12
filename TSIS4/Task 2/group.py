import re
s = input()
pattern = re.search(r'([a-zA-Z0-9])\1+', s)
if pattern:
    print(pattern.group(1))
else:
    print(-1)   
      