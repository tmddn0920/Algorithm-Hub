import sys
input = sys.stdin.readline

count = [0] * 8001

n = int(input())

for _ in range(n):
    count[int(input()) + 4000] += 1

max_count = max(count)
arr = []
max_arr = []

for i in range(8001):
    if count[i] != 0:
        for num in range(count[i]):
            arr.append(i - 4000)
    if count[i] == max_count:
        max_arr.append(i - 4000)

print(round(sum(arr) / n))
print(arr[n // 2])
if len(max_arr) == 1:
    print(max_arr[0])
else:
    print(max_arr[1])
print(arr[-1] - arr[0])