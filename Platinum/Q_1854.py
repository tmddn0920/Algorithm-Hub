import sys
import heapq
input = sys.stdin.readline

N, M, K = map(int, input().split())
distance = [[sys.maxsize] * K for _ in range(N + 1)]
A = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    A[a].append((b, c))
    
q = [(0, 1)]
distance[1][0] = 0

while q:
    temp_weight, temp_node = heapq.heappop(q)
    for node, weight in A[temp_node]:
        if distance[node][K - 1] > temp_weight + weight:
            distance[node][K - 1] = temp_weight + weight
            distance[node].sort()
            heapq.heappush(q, [temp_weight + weight, node])

for i in range(1, N + 1):
    if distance[i][K - 1] == sys.maxsize:
        print(-1)
    else:
        print(distance[i][K - 1])