def merge_sort(start, end):
    global A, Asort, result
    mid = int(start + (end - start) / 2)
    if end - start < 1:
        return
    merge_sort(start, mid)
    merge_sort(mid + 1, end)
    for i in range(start, end + 1):
        Asort[i] = A[i]
    num = start
    index_1 = start
    index_2 = mid + 1
    while index_1 <= mid and index_2 <= end:
        if Asort[index_1] > Asort[index_2]:
            A[num] = Asort[index_2]
            result = result + index_2 - num 
            num += 1
            index_2 += 1
        else:
            A[num] = Asort[index_1]
            num += 1
            index_1 += 1
    while index_1 <= mid:
        A[num] = Asort[index_1]
        num += 1
        index_1 += 1
    while index_2 <= end:
        A[num] = Asort[index_2]
        num += 1
        index_2 += 1
    
result = 0
N = int(input())
A = list(map(int, input().split()))
Asort = [0] * N
merge_sort(0, N - 1)
print(result)