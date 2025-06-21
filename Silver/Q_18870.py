N = int(input())
Arr = list(map(int, input().split()))
Sort_Arr = sorted(set(Arr))
Dic = {value: index for index, value in enumerate(Sort_Arr)}
Result_Arr = [Dic[num] for num in Arr]
for num in Result_Arr:
    print(num, end = " ")