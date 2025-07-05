def find(a, b):
    if b == 0:
        return a
    else:
        return find(b, a % b)
    
T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    result = a * b / find(a, b)
    print(int(result))