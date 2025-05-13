import sys
input = sys.stdin.readline

arr = [0] * 1001
arr[1] = 1
arr[2] = 2
arr[3] = 3

for num in range(4, 1001):
    arr[num] = arr[num - 1] + arr[num - 2]
    
num = int(input())
print(arr[num] % 10007)