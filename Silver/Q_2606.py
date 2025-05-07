computer = int(input())
network = int(input())

virus_arr = [1]
connections = []

for _ in range(network):
    a, b = map(int, input().split())
    connections.append([a, b])

changed = True
while changed:
    changed = False
    for a, b in connections:
        if a in virus_arr and b not in virus_arr:
            virus_arr.append(b)
            changed = True
        elif b in virus_arr and a not in virus_arr:
            virus_arr.append(a)
            changed = True

print(len(virus_arr) - 1)