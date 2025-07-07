A, B, C, x1, x2, y1, y2 = map(int, input().split())
count = 0
C = C * -1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
def extend(a, b):
    temp = [0] * 2
    if b == 0:
        temp[0] = 1
        temp[1] = 0
        return temp
    result = a // b
    arr = extend(b, a % b)
    temp[0] = arr[1]
    temp[1] = arr[0] - arr[1] * result
    return temp

if A == 0 and B == 0:
    if C == 0:
        count = (x2 - x1 + 1) * (y2 - y1 + 1)
    else:
        count = 0
    print(count)
    exit()
    
if A == 0:
    if C % B != 0:
        print(count)
        exit()
    y = C // B
    if y1 <= y <= y2:
        count = x2 - x1 + 1
        print(count)
    else:
        print(count)
    exit()

if B == 0:
    if C % A != 0:
        print(count)
        exit()
    x = C // A
    if x1 <= x <= x2:
        count = y2 - y1 + 1
        print(count)
    else:
        print(count)
    exit()

mgcd = gcd(A, B)

if C % mgcd != 0:
    print(0)
else:
    num = int(C / mgcd)
    result = extend(A, B)
    result[0] = result[0] * num
    result[1] = result[1] * num
    A = int(A // mgcd)
    B = int(B // mgcd)
    for i in range(x1, x2 + 1):
        if (i - result[0]) % B == 0:
            temp = (i - result[0]) // B
            if y1 <= result[1] - A * temp <= y2:
                count += 1
    print(count)