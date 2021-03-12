import re

txt = input()
match = re.findall(r'[^aeuio]([aeuioAEIOU]{2,})(?=[^aeuio])',txt)
if match:
    for i in match:
        print(i)
else:
    print(-1)        