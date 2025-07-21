N = int(input())

def Counting(num):
    Count = [0] * 10
    digit = 1
    while N // digit > 0:
        high = N // (digit * 10)
        now = (N // digit) % 10
        low = N % digit

        for i in range(10):
            Count[i] += high * digit

        if now > 0:
            for i in range(now):
                Count[i] += digit
            Count[now] += low + 1
        else:
            Count[0] += low + 1

        Count[0] -= digit 
        digit *= 10
    return Count
 
result = Counting(N)

for i in range(10):
    print(result[i], end = ' ')