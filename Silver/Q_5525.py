N = int(input())
M = int(input())
A = input()

index = 0
count = 0
result = 0

while index <= M - 3:
    if A[index:index + 3] == 'IOI':
        count += 1
        if count == N:
            result += 1
            count -= 1
        index += 2
    else:
        count = 0
        index += 1

print(result)