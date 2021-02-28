road = input()
x,y = map(int,input().split())

x1 = 0
y1 = 0
for i in road:
    if x1 != x and y1 != y:
        if i == "L":
            x1 -= 1
        elif i == "R":
            x1 += 1    
        elif i == "U":
            y1 += 1
        else:
            y1 -= 1
    else:
        print("passed")
        break    


