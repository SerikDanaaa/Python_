import re

txt = input()
txt1 = re.findall(r'\w', txt)
print(len(txt))
print(len(txt1))