while True:
    line = input()
    if line == '0 0 0':
        break
    arr = list(map(int, line.split()))
    arr.sort()
    if arr[0] ** 2 + arr[1] ** 2 == arr[2] ** 2:
        print('right')
    else:
        print('wrong')