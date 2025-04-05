score = 0.0
totalrate = 0
for i in range(0, 20):
    line = input()
    rate = line.split()
    if rate[2] == 'A+':
        score += float(rate[1]) * 4.5
    if rate[2] == 'A0':
        score += float(rate[1]) * 4.0
    if rate[2] == 'B+':
        score += float(rate[1]) * 3.5
    if rate[2] == 'B0':
        score += float(rate[1]) * 3.0
    if rate[2] == 'C+':
        score += float(rate[1]) * 2.5
    if rate[2] == 'C0':
        score += float(rate[1]) * 2.0
    if rate[2] == 'D+':
        score += float(rate[1]) * 1.5
    if rate[2] == 'D0':
        score += float(rate[1]) * 1.0
    if rate[2] == 'F':
        score += float(rate[1]) * 0.0
    if rate[2] != 'P':
        totalrate += float(rate[1])
print(score / totalrate)