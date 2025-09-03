N, K = map(int, input().split())
dp = [0] * (K + 1)

for _ in range(N):
    W, V = map(int, input().split())
    for num in range(K, W - 1, -1):
        dp[num] = max(dp[num], dp[num - W] + V)
        
print(dp[K])