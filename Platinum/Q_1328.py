import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
Building = [[[0] * 101 for _ in range(101)] for _ in range(101)]
Building[1][1][1] = 1
MOD = 1000000007

for i in range(2, N + 1):
    for j in range(1, L + 1):
        for k in range(1, R + 1):
            Building[i][j][k] = (Building[i - 1][j][k] * (i - 2)) + Building[i - 1][j - 1][k] + Building[i - 1][j][k - 1]

print(Building[N][L][R] % MOD)