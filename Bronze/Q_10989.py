import sys
input = sys.stdin.readline

count = [0] * 10001
n = int(input())
for _ in range(n):
    count[int(input())] += 1

for i in range(10001):
    if count[i]:
        for _ in range(count[i]):
            sys.stdout.write(f"{i}\n")