from itertools import permutations

N, M = map(int, input().split())
A = sorted(map(int, input().split()))
for num in permutations(A, M):
    print(*num)