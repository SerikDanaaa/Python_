n = int(input())
list1 = list(map(int,input().split()))
if list1.count(1) > 0:
    ok =False
else:
    ok = True
if ok:
    print("Clean :", list1.count(0))
    print("Dirty :", 0)

else:
    print("Clean :", 0)
    print("Dirty :", len(list1))        