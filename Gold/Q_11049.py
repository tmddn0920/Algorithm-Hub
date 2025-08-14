import sys
input = sys.stdin.readline

N = int(input())
matrix = []
dp = [[-1] * (N + 1) for _ in range(N + 1)]

matrix.append((0, 0))
for _ in range(N):
    r, c = map(int, input().split())
    matrix.append((r, c))
    
def multiple(start, end):
    result = sys.maxsize
    if dp[start][end] != -1:
        return dp[start][end]
    if start == end:
        return 0
    if start + 1 == end:
        return matrix[start][0] * matrix[start][1] * matrix[end][1]
    for i in range(start, end):
        result = min(result, matrix[start][0] * matrix[i][1] * matrix[end][1] + multiple(start, i) + multiple(i + 1, end))
    dp[start][end] = result
    return dp[start][end]

print(multiple(1, N))