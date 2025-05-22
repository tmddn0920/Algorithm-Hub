num = int(input())
count = 1
start_index = 1
end_index = 1
total_sum = 1

while start_index != num:
    if total_sum == num:
        count += 1
        end_index += 1
        total_sum += end_index
    elif total_sum > num:
        total_sum -= start_index
        start_index += 1
    elif total_sum < num:
        end_index += 1
        total_sum += end_index
print(count)
        