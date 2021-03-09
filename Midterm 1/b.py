import re
txt = input()
txt1 = re.findall(r'\w', txt)
print('Found a match !' if len(txt) == len(txt1) else 'Not matched !')