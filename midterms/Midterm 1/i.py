n = int(input())
a = list(map(int,input().split()))
a1 = sorted(a)
if a == a1:
    print("Interesting")
else:
    print("Not interesting")    