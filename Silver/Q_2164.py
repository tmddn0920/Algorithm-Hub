from collections import deque

num = int(input())
card = deque(range(1, num + 1))
    
while len(card) > 1:
    card.popleft()
    card.append(card.popleft())

print(card[0])