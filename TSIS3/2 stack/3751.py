a = set(map(int,input().strip().split()))
b = set(map(int,input().strip().split()))
print(*sorted(a&b))