arr = []

for i in range(0, 10):
    num = int(input())
    arr.append(num)
    
arr2 = []
for num in arr:
    arr2.append(num % 42)
unique_arr = list(set(arr2))
print(len(unique_arr))