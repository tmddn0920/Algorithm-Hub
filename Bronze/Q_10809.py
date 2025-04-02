line = input()
alp = "abcdefghijklmnopqrstuvwxyz"
for i in range(0, len(alp)):
    if alp[i] in line:
        for j in range(0, len(line)):
            if alp[i] == line[j]:
                print(j, end=" ")
                break
    else:
        print(-1, end=" ")