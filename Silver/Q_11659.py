import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0] * (m + 1)
for i in range(m):
    prefix_sum[i + 1] = prefix_sum[i] + arr[i]

for _ in range(n):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])