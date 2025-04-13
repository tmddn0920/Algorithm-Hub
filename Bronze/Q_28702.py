arr = []
for num in range(0, 3):
    line = input()
    if line == "Fizz" or line == "Buzz" or line == "FizzBuzz":
        arr.append(0)
    else:
        line = int(line)
        arr.append(line)
result = 0
for num in range(0, 3):
    if arr[num] != 0:
        result = arr[num] + 3 - num
if result % 3 == 0 and result % 5 == 0:
    print("FizzBuzz")
elif result % 3 == 0 and result % 5 != 0:
    print("Fizz")
elif result % 3 != 0 and result % 5 == 0:
    print("Buzz")
else:
    print(result)