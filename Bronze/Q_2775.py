num = int(input())
for case in range(0, num):
    total = 0
    a = int(input())
    b = int(input())
    arr = [[0] * b for _ in range(a + 1)]
    for i in range(0, a + 1):
        for j in range(0, b):
            if i == 0:
                arr[i][j] = j + 1
            elif i != 0:
                sum = 0
                for k in range(0, j + 1):
                    sum += arr[i - 1][k]
                arr[i][j] = sum
    print(arr[a][b - 1])
            
                