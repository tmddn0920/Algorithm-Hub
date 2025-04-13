num = '665'
count = 0
series = int(input())
while True:
    num = str(int(num) + 1)
    if '666' in num:
        count += 1
    if count == series:
        break
print(num)