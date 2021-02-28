n = int(input())
list1 = list(map(int,input().strip().split()))
st = set(list1)
if len(st) != n:
    print("NO")
else:
    print("YES")        
   
