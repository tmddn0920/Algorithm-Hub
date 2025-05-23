N = int(input())
arr = []
blue = 0
white = 0

def calculate(X, Y, N):
    global arr, blue, white
    isClear = True
    color = arr[X][Y]
    for num_X in range(N):
        for num_Y in range(N):
            if arr[X + num_X][Y + num_Y] != color:
                isClear = False
    if isClear == False:
        calculate(X, Y, N // 2)
        calculate(X + N // 2, Y, N // 2)
        calculate(X, Y + N // 2, N // 2)
        calculate(X + N // 2, Y + N // 2, N // 2)
    if isClear == True:
        if color == 1:
            blue += 1
        elif color == 0:
            white += 1

for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    
calculate(0, 0, N)

print(white)
print(blue)