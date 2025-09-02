from itertools import permutations

N, M = map(int, input().split())
Arr = list(map(int, input().split()))
Arr.sort()
result = set(permutations(Arr, M))
for num in sorted(result):
    print(*num)