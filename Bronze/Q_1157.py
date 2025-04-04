from collections import Counter

str = input()
cap_str = str.upper()
counter = Counter(cap_str)
max_count = max(counter.values())
most_common_letters = [char for char, count in counter.items() if count == max_count]
if len(most_common_letters) > 1:
    print("?")
else:
    print(most_common_letters[0])