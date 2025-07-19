import copy
import sys
from collections import deque
from queue import PriorityQueue

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
A = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(N):
    A[i] = list(map(int, input().split()))
    
country = 1
country_list = list([])
ground_list = []

def addGround(i, j, queue):
    A[i][j] = country
    visited[i][j] = True
    ground_list.append([i, j])
    queue.append([i, j])
    
def BFS(i, j):
    queue = deque()
    ground_list.clear()
    queue.append([i, j])
    ground_list.append([i, j])
    visited[i][j] = True
    A[i][j] = country
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and A[nx][ny] != 0:
                    addGround(nx, ny, queue)
    return ground_list

for i in range(N):
    for j in range(M):
        if A[i][j] == 1 and not visited[i][j]:
            ground = copy.deepcopy(BFS(i, j))
            country_list.append(ground)
            country += 1
            
pq = PriorityQueue()

for current_ground in country_list:
    for temp in current_ground:
        x = temp[0]
        y = temp[1]
        current_country = A[x][y]
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            bridge_len = 0
            while 0 <= nx < N and 0 <= ny < M:
                if A[nx][ny] == current_country:
                    break
                if A[nx][ny] != 0:
                    if bridge_len >= 2:
                        target_country = A[nx][ny]
                        pq.put((bridge_len, current_country, target_country))
                    break
                nx += dx[d]
                ny += dy[d]
                bridge_len += 1
                
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
        
parent = [0] * country

for i in range(len(parent)):
    parent[i] = i
    
count = 0
result = 0

while pq.qsize() > 0:
    length, start, end = pq.get()
    if find(start) != find(end):
        union(start, end)
        result += length
        count += 1
        
if count == country - 2:
    print(result)
else:
    print(-1)