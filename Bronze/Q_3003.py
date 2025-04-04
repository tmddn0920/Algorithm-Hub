dong_arr = []
dong_arr = input().split()
org_arr = [1, 1, 2, 2, 2, 8]
for i in range(0, len(dong_arr)):
    print(int(org_arr[i]) - int(dong_arr[i]), end=" ")