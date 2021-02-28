import re
txt = input()
word = input()

find = re.search(word,txt)
if find:
    print("First time Polinoma occured in position:",find.start())
else:
    print("Not found")    