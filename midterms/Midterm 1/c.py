n = int(input())
list1 = list(map(int,input().split()))
st = set(list1)
list1.sort()
for i in range(0,len(st)):
    print(i+1 ,list1[i] )
