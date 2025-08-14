import sys
input = sys.stdin.readline

N = int(input())
weight = []

for _ in range(N):
    weight.append(list(map(int, input().split())))
    
dp = [[0] * (1 << 16) for _ in range(16)]

def tsp(c, v):
    if v == (1 << N) - 1:
        if weight[c][0] == 0:
            return float('inf')
        else:
            return weight[c][0]
    if dp[c][v] != 0:
        return dp[c][v]
    result = float('inf')
    for i in range(0, N):
        if (v & (1 << i)) == 0 and weight[c][i] != 0:
            result = min(result, tsp(i, (v | (1 << i))) + weight[c][i])
    dp[c][v] = result
    return dp[c][v]

print(tsp(0, 1))