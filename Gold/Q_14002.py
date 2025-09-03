import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)

index = 0
maxLength = 1
temp = [0] * 1000001
result = [0] * 1000001
dp = [0] * 1000001
temp[maxLength] = A[1]
dp[1] = 1

def binarySearch(left, right, now):
    while left < right:
        mid = (left + right) // 2
        if temp[mid] < now:
            left = mid + 1
        else:
            right = mid
    return left

for i in range(2, N + 1):
    if temp[maxLength] < A[i]:
        maxLength += 1
        temp[maxLength] = A[i]
        dp[i] = maxLength
    else:
        index = binarySearch(1, maxLength, A[i])
        temp[index] = A[i]
        dp[i] = index

print(maxLength)
index = maxLength

for i in range(N, 0, -1):
    if dp[i] == index:
        result[index] = A[i]
        index -= 1

for i in range(1, maxLength + 1):
    print(result[i], end=" ")