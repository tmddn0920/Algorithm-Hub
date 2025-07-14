from collections import deque

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    A = [[] for _ in range(N + 1)]
    degree = [0] * (N + 1)
    result = [0] * (N + 1)

    for _ in range(K):
        X, Y = map(int, input().split())
        A[X].append(Y)
        degree[Y] += 1

    W = int(input())

    queue = deque()
    for i in range(1, N + 1):
        if degree[i] == 0:
            queue.append(i)
            result[i] = time[i]

    while queue:
        temp = queue.popleft()
        for i in A[temp]:
            degree[i] -= 1
            result[i] = max(result[i], result[temp] + time[i])
            if degree[i] == 0:
                queue.append(i)

    print(result[W])