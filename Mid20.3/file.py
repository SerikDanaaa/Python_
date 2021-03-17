with open('input.txt','r') as f:
   mylist = f.readlines()
   cnt = 0
   for i in range(len(mylist)):
       cnt += 1
print(cnt)        

