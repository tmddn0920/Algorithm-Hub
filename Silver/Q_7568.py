n = int(input())
arr = [[0, 0] for _ in range(n)]
for i in range(0, n):
    weight, height = map(int, input().split())
    arr[i][0] = weight
    arr[i][1] = height
score = [1] * n
for i in range(0, n):
    for j in range(0, n):
        if i != j:
            if arr[i][0] < arr[j][0]:
                if arr[i][1] < arr[j][1]:
                    score[i] += 1
for i in range(0, n):
    print(score[i], end=" ")