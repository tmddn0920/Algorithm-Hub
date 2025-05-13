dp = [0] * 1001
dp[1] = 1
dp[2] = 3

for num in range(3, 1001):
    dp[num] = dp[num - 1] + 2 * dp[num - 2]
    
num = int(input())
print(dp[num] % 10007)