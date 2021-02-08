n = int(input())

h = n//3600
m = (n- h*3600)//60

h = str(h)
m = str(m)

print("It is " + h + " hours " + m + " minutes.")
