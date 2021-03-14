import re
user = input()
password = input()
userpattern = re.search(r'\w.*#\d{4}$',user)
passwordpattern = re.search(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*\W)', password)
if passwordpattern and userpattern:
    print("YES")
else:
    print("No")    