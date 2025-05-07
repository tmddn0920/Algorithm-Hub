import sys
input = sys.stdin.readline

stair = int(input())
arr = []

for _ in range(stair):
    num = int(input())
    arr.append(num)

def upToStair():
    global arr
    if stair == 1:
        print(arr[0])
        return
    if stair == 2:
        print(arr[0] + arr[1])
        return
    dp = [0] * stair
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    for i in range(2, stair):
        dp[i] = max(arr[i] + dp[i - 2], arr[i] + arr[i - 1] + dp[i - 3])
    print(dp[stair - 1])
    
upToStair()