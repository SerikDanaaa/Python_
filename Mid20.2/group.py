inlist = set(input().split())
ingroup = set(input().split())
absent = set()
lost = set()
for i in inlist:
    if i not in ingroup:
        absent.add(i)
for i in ingroup:
    if i not in inlist:
        lost.add(i)
print("Absent : ", *absent)
print("Lost : ", *lost)                

