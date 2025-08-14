import sys
input = sys.stdin.readline

dp = [[[sys.maxsize] * 5 for _ in range(5)] for _ in range(100001)]
power = [[0, 2, 2, 2, 2],
         [2, 1, 3, 4, 3],
         [2, 3, 1, 3, 4],
         [2, 4, 3, 1, 3],
         [2, 3, 4, 3, 1]]

index = 0
dp[0][0][0] = 0
inputList = list(map(int, input().split()))

while inputList[index] != 0:
    n = inputList[index]
    for i in range(5):
        if n == i:
            continue
        for j in range(5):
            dp[index + 1][i][n] = min(dp[index][i][j] + power[j][n], dp[index + 1][i][n])
        
        for j in range(5):
            if n == j:
                continue
            for i in range(5):
                dp[index + 1][n][j] = min(dp[index][i][j] + power[i][n], dp[index + 1][n][j])
    index += 1
    
result = sys.maxsize
for i in range(5):
    for j in range(5):
        result = min(result, dp[index][i][j])
        
print(result)