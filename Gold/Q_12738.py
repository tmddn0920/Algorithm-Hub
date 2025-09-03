import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

temp = [0] * (N + 1) 
maxLength = 0

def binarySearch(left, right, now):
    while left < right:
        mid = (left + right) // 2
        if temp[mid] < now:
            left = mid + 1
        else:
            right = mid
    return left

for x in A:
    if maxLength == 0 or temp[maxLength] < x:
        maxLength += 1
        temp[maxLength] = x
    else:
        idx = binarySearch(1, maxLength, x)
        temp[idx] = x

print(maxLength)