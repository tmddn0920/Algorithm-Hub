num = int(input())

if num < 2:
    print(1)
else:
    arr = [0] * num
    arr[1] = 1
    now = 1

    for number in range(2, num + 1):
        count = 0
        while count != number + 1:
            now += 1
            if now < num:
                if arr[now] == 0:
                    count += 1
            else:
                now = 0
                if arr[0] == 0:
                    count += 1
        arr[now] = number

    for i in range(len(arr)):
        print(arr[i], end=" ")