import re
print("Founf a match !" if re.findall(r'[A-Z][a-z]+', input()) else 'Not matched !' )