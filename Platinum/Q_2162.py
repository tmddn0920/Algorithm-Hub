N = int(input())
parent = [-1] * (3001)

def CCW(x1, y1, x2, y2, x3, y3):
    result = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
    if result > 0:
        return 1
    elif result < 0:
        return -1
    return 0

def isSame(x1, y1, x2, y2, x3, y3, x4, y4):
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) \
        and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
            return True
    return False

def isCross(x1, y1, x2, y2, x3, y3, x4, y4):
    abc = CCW(x1, y1, x2, y2, x3, y3)
    abd = CCW(x1, y1, x2, y2, x4, y4)
    cda = CCW(x3, y3, x4, y4, x1, y1)
    cdb = CCW(x3, y3, x4, y4, x2, y2)
    if abc * abd == 0 and cda * cdb == 0:
        return isSame(x1, y1, x2, y2, x3, y3, x4, y4)
    elif abc * abd <= 0 and cda * cdb <= 0:
        return True
    return False

def find(a):
    if parent[a] < 0:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    if parent_a == parent_b:
        return
    parent[parent_a] += parent[parent_b]
    parent[parent_b] = parent_a
    
A = []
A.append([])

for i in range(1, N + 1):
    A.append(list(map(int, input().split())))
    for j in range(1, i):
        if isCross(A[i][0], A[i][1], A[i][2], A[i][3], A[j][0], A[j][1], A[j][2], A[j][3]):
            union(i, j)
            
result = 0
count = 0

for i in range(1, N + 1):
    if parent[i] < 0:
        count += 1
        result = min(result, parent[i])
        
print(count)
print(-result)