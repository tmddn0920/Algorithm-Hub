line = input()
arr = line.split('-')

result = sum(map(int, arr[0].split('+')))

for part in arr[1:]:
    result -= sum(map(int, part.split('+')))

print(result)