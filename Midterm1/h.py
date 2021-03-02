n = int(input())
inlist = list(map(str,input().split()))
m = int(input())
group = list(map(str,input().split()))

mis = list()
notin = list()

for i in inlist:
    if i not in group:
        mis.append(i)

for i in group:
    if i not in inlist:
        notin.append(i)

print("Missed students:")
for i in mis:
    print(" - ", i)
    
print("Not in the group:")
for i in notin:
    print(" - ", i)    