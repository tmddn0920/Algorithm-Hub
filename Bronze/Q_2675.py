num = int(input())
for i in range(0, num):
    count, line = map(str, input().split())
    count = int(count)
    for j in range(0, len(line)):
        print(line[j] * count, end="")
    print()
    