num = int(input())
for _ in range(num):
    line = input()
    real_line = []
    number = int(len(line) ** 0.5)
    for n in range(number):
        n = number - n - 1
        for i in range(number):
            real_line.append(line[n + (number * i)])
    for word in real_line:
        print(word, end="")
    print()