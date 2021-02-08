n = int(input())

h = n //30
m = (n*2)-(60*((n*2)//60))

h = str(h)
m = str(m)
print( "It is " + h +" hours " + m + " minutes.")