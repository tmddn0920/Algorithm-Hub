num = int(input())
Num_Arr = list(map(int, input().split()))
Stack = []
Result_Arr = [0] * num

for index in range(0, num):
    while Stack and Num_Arr[index] > Num_Arr[Stack[-1]]:
        n = Stack.pop()
        Result_Arr[n] = Num_Arr[index]
    Stack.append(index)

if Stack:
    for n in Stack:
        Result_Arr[n] = -1
        
for number in Result_Arr:
    print(number, end = " ")