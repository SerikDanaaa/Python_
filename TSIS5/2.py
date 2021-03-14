n = int(input())
while n:
    with open('test.txt', 'r') as f:
        print(f.readline())
        n -= 1
