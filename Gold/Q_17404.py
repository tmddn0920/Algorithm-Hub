import sys
input = sys.stdin.readline

INF = 10**9

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

result = INF
for start in range(3): 
    dp = [[INF]*3 for _ in range(N)]
    dp[0][start] = cost[0][start] 

    for i in range(1, N):
        dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

    for last in range(3):
        if last == start:
            continue
        result = min(result, dp[N-1][last])

print(result)