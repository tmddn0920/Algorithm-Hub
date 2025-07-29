N = int(input())
question = list(map(int, input().split()))
Count = [0] * 21
A = [0] * 21
visited = [False] * 21

Count[0] = 1
for i in range(1, N + 1):
    Count[i] = Count[i - 1] * i

if question[0] == 1:
    K = question[1]
    for i in range(1, N + 1):
        num = 1
        for j in range(1, N + 1):
            if visited[j]:
                continue
            if K <= num * Count[N - i]:
                K -= (num - 1) * Count[N - i]
                A[i] = j
                visited[j] = True
                break
            num += 1
    for i in range(1, N + 1):
        print(A[i], end = " ")
        
else:
    K = 1
    for i in range(1, N + 1):
        num = 0
        for j in range(1, question[i]):
            if not visited[j]:
                num += 1
        K += num * Count[N - i]
        visited[question[i]] = True
    print(K)