def PointInSquare(x, y):
    return abs(x) <= 1 and y == 0 or abs(y) <= 1 and x == 0 or abs(x) <= 0.5 and abs(y) <= 0.5

x, y = float(input()), float(input())
if PointInSquare(x, y):
    print('YES')
else:
    print('NO')