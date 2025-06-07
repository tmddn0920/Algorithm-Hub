line = input()
zero = 0
one = 0
status = line[0]
if status == '1':
    one += 1
else:
    zero += 1
for n in range(1, len(line)):
    if line[n] != status:
        status = line[n]
        if line[n] == '1':
            one += 1
        else:
            zero += 1
print(min(one, zero))