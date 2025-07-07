N = int(input())
A = [[] for _ in range(N)]
Visited = [False] * N
Num = [0] * N
lcm = 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def DFS(v):
    Visited[v] = True
    for i in A[v]:
        j = i[0]
        if not Visited[j]:
            Num[j] = Num[v] * i[2] // i[1]
            DFS(j)

for i in range(N - 1):
    a, b, p, q = map(int, input().split())
    A[a].append((b, p, q))
    A[b].append((a, q, p))
    lcm *= (p * q // gcd(p, q))

Num[0] = lcm
DFS(0)
devider = Num[0]

for i in range(1, N):
    devider = gcd(devider, Num[i])
    
for i in range(N):
    print(int(Num[i] / devider), end = " ")