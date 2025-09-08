N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

dp_w = [[0] * N for _ in range(N)]
dp_h = [[0] * N for _ in range(N)]
dp_c = [[0] * N for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for i in range(0, N):
    for j in range(1, N):
        if A[i][j] != 1:
            dp_w[i][j] = dp_w[i][j - 1] + dp_c[i][j - 1]
            if i == 0 and j == 1:
                dp_w[i][j] = 1
        if i >= 1 and A[i][j] != 1:    
            dp_h[i][j] = dp_h[i - 1][j] + dp_c[i - 1][j]
        if i >= 1 and A[i - 1][j] != 1 and A[i][j - 1] != 1 and A[i][j] != 1:
            dp_c[i][j] = dp_w[i - 1][j - 1] + dp_h[i - 1][j - 1] + dp_c[i - 1][j - 1]

print(dp_w[N - 1][N - 1] + dp_h[N - 1][N - 1] + dp_c[N - 1][N - 1])