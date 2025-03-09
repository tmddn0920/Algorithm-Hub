total_price = int(input())
total_num = int(input())
result = 0
price = 0
for num in range(total_num):
    A, B = map(int, input().split())
    price = A * B
    result = result + price
if(result == total_price):
    print('Yes')
else:
    print('No')