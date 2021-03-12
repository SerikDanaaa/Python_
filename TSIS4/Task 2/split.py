import re
s = input()

res = re.sub(r'[,|.]','\n', s)
print(res)