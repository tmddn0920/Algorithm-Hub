from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

left = 0
count = defaultdict(int)
Max = 0

for right in range(N):
    count[A[right]] += 1
    
    while len(count) > 2:
        count[A[left]] -= 1
        if count[A[left]] == 0:
            del count[A[left]]
        left += 1
    Max = max(Max, right - left + 1)

print(Max)