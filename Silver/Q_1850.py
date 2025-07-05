def find(a, b):
    if b == 0:
        return a
    else:
        return find(b, a % b)
    
a, b = map(int, input().split())
result = find(a, b)

while result > 0:
    print('1', end = '')
    result -= 1