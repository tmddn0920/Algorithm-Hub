repeat = True
while repeat:    
    line = input()
    if line == '0':
        break
    isPel = True
    for i in range(0, len(line)):
        total = len(line) - 1
        if line[i] != line[total - i]:
            isPel = False
    if isPel == True:
        print('yes')
    elif isPel == False:
        print('no')