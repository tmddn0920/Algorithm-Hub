from collections import Counter

n = int(input())
arr = input().split()

m = int(input())
num = input().split()

counter = Counter(arr)

for x in num:
    print(counter[x], end=' ')