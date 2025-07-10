N = int(input())
M = int(input())
city = [[0] * (N + 1) for _ in range(N + 1)]

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
        
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

for i in range(1, N + 1):
    city[i] = list(map(int, input().split()))
    city[i].insert(0, 0)
    
travel = list(map(int, input().split()))
travel.insert(0, 0)

parent = [0] * (N + 1)

for i in range(1, N + 1):
    parent[i] = i

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if city[i][j] == 1:
            union(i, j)

result = True
parent_travel = find(travel[1])
for i in range(2, len(travel)):
    if find(travel[i]) != parent_travel:
        result = False
        break
        
if result:
    print('YES')
else:
    print('NO')