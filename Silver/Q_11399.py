import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))
time = sorted(time)
result = 0

for i in range(n):
    for j in range(i + 1):
        result = result + time[j]     

print(result)