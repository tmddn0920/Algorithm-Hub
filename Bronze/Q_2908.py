line = input()
a, b = map(str, line.split())
reverse_a = ""
for i in a:
    reverse_a = i + reverse_a
reverse_b = ""
for i in b:
    reverse_b = i + reverse_b
if int(reverse_a) > int(reverse_b):
    print(reverse_a)
else:
    print(reverse_b)