N, M = map(int, input().split())
parent = [0] * (N + 1)

def find(num):
    if num == parent[num]:
        return num
    else:
        parent[num] = find(parent[num])
        return parent[num]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def isSame(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for i in range(1, N + 1):
    parent[i] = i
    
for _ in range(M):
    digit, a, b = map(int, input().split())
    if digit == 0:
        union(a, b)
    elif digit == 1:
        if isSame(a, b):
            print('YES')
        else:
            print('NO')