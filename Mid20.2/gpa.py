n = int(input())
names = dict()
while n:
    name, gpa = input().split()
    if not names.get(name):
        names[name] = [1,0]
    else:
        names[name][0] += 1
        names[name][1] += gpa 
for name in sorted(names):
    avg_gpa = names[name][1] / names[name][0]           
    print(name, ": ", f'{avg_gpa:.3f}',sep='')







