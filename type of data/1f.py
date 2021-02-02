a,b,c = map(int,input().split())
d,e,f = map(int,input().split())

ans = -(3600*a+60*b+c)+(3600*d+60*e+f)
print( ans )
