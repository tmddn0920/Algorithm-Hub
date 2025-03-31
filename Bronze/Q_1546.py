num_test = int(input())
score = input().split()
total = 0
for i in range(0, num_test):
    score[i] = float(score[i])
    total += score[i]
max_score = max(score)
new_total = 0
for i in range(0, num_test):
    score[i] = score[i] / max_score
    score[i] = score[i] * 100
    new_total += score[i]
mean = new_total / num_test
print(mean)