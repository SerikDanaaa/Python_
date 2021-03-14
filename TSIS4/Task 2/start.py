import re
txt = input()
a = input()
match = re.findall(a,txt)
if match:
    for i in match:
        print(match.start(), match.end())
else:
    print(-1,-1)        