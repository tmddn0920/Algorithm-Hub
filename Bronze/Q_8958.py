num = int(input())
for i in range(0, num):
    line = input()
    count = 0
    score = 0
    for j in range(0, len(line)):
        if line[j] == 'O':
            count += 1
            score += count
        elif line[j] == 'X':
            count = 0
    print(score)