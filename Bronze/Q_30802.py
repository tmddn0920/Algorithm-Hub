import math

n = int(input())
arr = list(map(int, input().split()))
t, p = map(int, input().split())
total_t = 0
for num in arr:
    total_t += math.ceil(num / t)
print(total_t)
print(n // p, end=" ")
print(n % p)