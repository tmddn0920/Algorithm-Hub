N, M = map(int, input().split())
truth = list(map(int, input().split()))
truth_num = truth[0]
del truth[0]
result = 0
party = [[] for _ in range(M)]

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
        
def isSmae(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for i in range(M):
    party[i] = list(map(int, input().split()))
    del party[i][0]
    
parent = [0] * (N + 1)

for i in range(N + 1):
    parent[i] = i

for i in range(M):
    temp = party[i][0]
    for j in range(1, len(party[i])):
        union(temp, party[i][j])

for i in range(M):
    isOkay = True
    temp = party[i][0]
    for j in range(len(truth)):
        if find(temp) == find(truth[j]):
            isOkay = False
            break
    if isOkay:
        result += 1

print(result)