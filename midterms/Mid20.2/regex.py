import re
user = input()
password = input()
passwordpattern = re.search(r'.*#\d{4}$',password)
userpattern = re.search(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W)', user)
if passwordpattern and userpattern:
    print("YES")
else:
    print("No")    