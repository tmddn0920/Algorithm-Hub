num = int(input())
line = input()
result = 0
M = 1234567891

for i in range(num):
    result += (ord(line[i]) - 96) * (31 ** i)
    result %= M  

print(result)