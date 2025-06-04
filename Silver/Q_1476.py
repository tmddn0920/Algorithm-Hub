E, S, M = map(int, input().split())
Year = 1

if E == 15:
    E = 0
if S == 28:
    S = 0
if M == 19:
    M = 0

while True:
    if Year % 15 == E:
        if Year % 28 == S:
            if Year % 19 == M:
                break
    Year += 1

print(Year)