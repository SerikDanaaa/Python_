list1 = list(map(int,input().split()))
list2 = list1.copy()
list2.sort()
cnt = 0
for i in range(len(list1)):
    if list1[i] != list2[i]:
        cnt += 1

print(cnt)        
