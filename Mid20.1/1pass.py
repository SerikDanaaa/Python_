import re

txt = input()
pattern = re.search(r'(1299|1[3-8]\d{2}|19[0-1]\d|192[0-2])\s(0[1-9]|1[0-2])\s(0[1-9]|[1-2]\d|30|31)',txt)

if pattern:print("YES")
else:print("NO")