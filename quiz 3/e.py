txt = input().split()

mx = 0
mxtxt = ""

for i in txt:
    if len(i) > mx:
       mx = len(i)
       mxtxt = i

print(mx)   
print(mxtxt)   