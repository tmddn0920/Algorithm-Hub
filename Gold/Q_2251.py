from collections import deque

send = [0, 0, 1, 1, 2, 2]
receive = [1, 2, 0, 2, 0, 1]
volume = list(map(int, input().split()))
visited = [[False] * 201 for _ in range(201)]
result = [False] * 201

def BFS():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    result[volume[2]] = True
    while queue:
        current_node = queue.popleft()
        A = current_node[0]
        B = current_node[1]
        C = volume[2] - A - B
        for i in range(6):
            next_node = [A, B, C]
            next_node[receive[i]] += next_node[send[i]]
            next_node[send[i]] = 0
            if next_node[receive[i]] > volume[receive[i]]:
                next_node[send[i]] = next_node[receive[i]] - volume[receive[i]]
                next_node[receive[i]] = volume[receive[i]]
            if not visited[next_node[0]][next_node[1]]:
                visited[next_node[0]][next_node[1]] = True
                queue.append((next_node[0], next_node[1]))
                if next_node[0] == 0:
                    result[next_node[2]] = True
                    
BFS()

for i in range(len(result)):
    if result[i]:
        print(i, end = " ")