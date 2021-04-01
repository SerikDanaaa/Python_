txt = input().split()
names = dict()
for name in txt:
    if not name in names:
        names[name] = 1       
    else:
        names[name] += 1
for name in sorted(names):
    print(name, names[name])
