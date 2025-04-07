num = int(input())
for i in range(0, num):
    a, b, c = map(int, input().split())
    floor = c % a
    room_no = c // a + 1
    if floor == 0:
        floor = a
        room_no -= 1
    print(floor * 100 + room_no)
