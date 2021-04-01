import re
date = input()
pattern = re.search(r'(1299|1[3-8]\d{2}|19[0-1]\d|192[0-2])\s(0[1-9]|1[1-2])\s([0-2][0-9]|30|31)',date)
if pattern:
    print("yes")
else:
    print("no")    