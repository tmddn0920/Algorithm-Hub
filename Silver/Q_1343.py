Arr = list(input())
Index = 0

while Index < len(Arr):
    if Arr[Index] == 'X':
        Count = 1
        while Index + Count < len(Arr) and Arr[Index + Count] == 'X':
            Count += 1
        
        if Count % 2 == 1:
            print(-1)
            break
        else:
            A = Count // 4
            B = (Count % 4) // 2
            for N in range(A * 4):
                Arr[Index + N] = 'A'
            for N in range(B * 2):
                Arr[Index + A * 4 + N] = 'B'
        
        Index += Count
    else:
        Index += 1
else:
    print(''.join(Arr))