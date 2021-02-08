n = int(input())
mult = 1
sum = 0
while n != 0:
   mult*= n%10
   sum+= n%10
   n//=10
print (mult-sum)    



