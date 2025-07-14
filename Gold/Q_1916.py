import sys
from queue import PriorityQueue

N = int(input())
M = int(input())
A = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
distance = [sys.maxsize] * (N + 1)
q = PriorityQueue()

for _ in range(M):
    u, v, w = map(int, input().split())
    A[u].append((v, w))

start, end = map(int, input().split())

q.put((0, start))
distance[start] = 0

while q.qsize() > 0:
    temp = q.get()
    temp_v = temp[1]
    if visited[temp_v]:
        continue
    visited[temp_v] = True
    for i in A[temp_v]:
        next_v = i[0]
        next_weight = i[1]
        if distance[next_v] > distance[temp_v] + next_weight:
            distance[next_v] = distance[temp_v] + next_weight
            q.put((distance[next_v], next_v))
            
print(distance[end])