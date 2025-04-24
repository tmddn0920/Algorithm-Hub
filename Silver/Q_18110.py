import sys

num = int(sys.stdin.readline())
arr = [0] * 30
for number in range(num):
    score = int(sys.stdin.readline())
    arr[score - 1] += 1
average = int((num * 0.15) + 0.5)
result_arr = []
for number in range(len(arr)):
    if arr[number] != 0:
        while arr[number] != 0:
            result_arr.append(number + 1)
            arr[number] -= 1
result = 0
for number in range(average, num - average):
    result += result_arr[number]
if num - (2 * average) == 0:
    print(0)   
else:
    print(int(result / (num - (2 * average)) + 0.5))
