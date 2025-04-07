line = input()
arr = line.split()
isAscend = 0
for i in range(0, len(arr)):
    if i < len(arr) - 1 and isAscend != 3:
        if int(arr[i]) == 8:
            if int(arr[i + 1]) != 1 and int(arr[i + 1]) != 7:
                print('mixed')
                isAscend = 3
                break
            elif int(arr[i + 1]) == 1:
                isAscend = 1
        elif int(arr[i]) + 1 == int(arr[i + 1]):
            isAscend = 1
        elif int(arr[i]) - 1 == int(arr[i + 1]):
            isAscend = 2
        elif int(arr[i]) == 1:
            if int(arr[i + 1]) != 8 and int(arr[i + 1] != 2):
                print('mixed')
                isAscend = 3
            elif int(arr[i + 1]) == 8:
                isAscend = 2
        else:
            print('mixed')
            isAscend = 3
            break
if isAscend == 1:
    print('ascending')
elif isAscend == 2:
    print('descending')
        