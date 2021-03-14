import re
inlist = list(map(str,input().split()))
ingroup = list(map(str,input().split()))
absent = list()
lost = list()
for i in inlist:
    
    find = re.search(i, ingroup)
    if not find:
        absent.append(i)
for i in ingroup:
    find1 = re.search(i, inlist)
    if not find1:
        lost.append(i)        

print("Absent : ", sorted(absent))
print("Lost : ", sorted(lost))     