N = int(input())
A = [[0] * 2 for _ in range(N)]

for num in range(N):
    start, end = map(int, input().split())
    A[num][0] = end
    A[num][1] = start
    
A.sort()
result = 0
end = -1

for num in range(N):
    if A[num][1] >= end:
        result += 1
        end = A[num][0]
        
print(result)