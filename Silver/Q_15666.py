from itertools import combinations_with_replacement

N, M = map(int, input().split())
Arr = sorted(set(map(int, input().split()))) 

for num in combinations_with_replacement(Arr, M):
    print(*num)