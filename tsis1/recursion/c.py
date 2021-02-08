  
def PointInSquare(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1

x, y = float(input()), float(input())
if PointInSquare(x, y):
    print('YES')
else:
    print('NO')