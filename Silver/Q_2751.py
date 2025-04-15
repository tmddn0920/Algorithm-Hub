import sys
input = sys.stdin.readline

n = int(input())
offset = 1000000
count = [0] * (2 * offset + 1)
for _ in range(n):
    num = int(input())
    count[num + offset] += 1
for i in range(2 * offset + 1):
    if count[i]:
        print(i - offset)