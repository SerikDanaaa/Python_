k,n = map(int, input().split())
i=0
while (n-k)>0:
    n-=k
    i+=1
if n != 0 :
    i+=1

print (str(i)+" "+str(n))       

