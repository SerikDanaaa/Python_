  
def PointInCircle(x, y):
    return (x - xc) ** 2 + (y - yc) ** 2 <= r * r

x, y, xc, yc, r = float(input()), float(input()), float(input()), float(input()), float(input())
if PointInCircle(x, y):
    print('YES')
else:
    print('NO')