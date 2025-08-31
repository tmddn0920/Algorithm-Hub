from collections import deque
import sys

N, M = map(int, input().split())
A = [-1 for _ in range(101)]

for _ in range(N):
    X, Y = map(int, input().split())
    A[X] = Y

for _ in range(M):
    U, V = map(int, input().split())
    A[U] = V
    
queue = deque([1])
visited = [False] * 101
visited[1] = True
level = 0

while queue:
    for _ in range(len(queue)):
        node = queue.popleft()
        if node == 100:
            print(level)
            sys.exit(0)
        for i in range(1, 7):
            next_node = node + i
            if next_node > 100:
                continue
            if A[next_node] != -1:      
                next_node = A[next_node]
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
    level += 1