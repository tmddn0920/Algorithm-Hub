import sys
sys.setrecursionlimit(100000)

N = int(input())
A = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    start, end, weight = map(int, input().split())
    A[start].append((end, weight))
    A[end].append((start, weight))
    
visited = [False] * (N + 1)

def DFS(start, distance):
    visited[start] = True
    far_node, max_distance = start, distance
    for node, weight in A[start]:
        if not visited[node]:
            next_node, next_distance = DFS(node, distance + weight)
            if next_distance > max_distance:
                far_node, max_distance = next_node, next_distance
    return far_node, max_distance

temp, _ = DFS(1, 0)
visited = [False] * (N + 1)
result_node, result_distance = DFS(temp, 0)
print(result_distance)