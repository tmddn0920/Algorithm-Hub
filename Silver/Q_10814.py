num = int(input())
member = [[''] for _ in range(200)]
for i in range(0, num):
    age, name = map(str, input().split())
    if member[int(age) - 1][0] == '':
        member[int(age) - 1][0] = name
    else:
        member[int(age) - 1].append(name)
for age in range(0, 200):
    for name in member[age]:
        if name != '':
            print(age + 1, name)