MyList = [0] * 4
SecretList = [0] * 4
Solve = 0
Count = 0

def add_list(c):
    global MyList, SecretList, Solve
    if c == 'A':
        MyList[0] += 1
        if MyList[0] == SecretList[0]:
            Solve += 1
    elif c == 'C':
        MyList[1] += 1
        if MyList[1] == SecretList[1]:
            Solve += 1
    elif c == 'G':
        MyList[2] += 1
        if MyList[2] == SecretList[2]:
            Solve += 1
    elif c == 'T':
        MyList[3] += 1
        if MyList[3] == SecretList[3]:
            Solve += 1
            
def sub_list(c):
    global MyList, SecretList, Solve
    if c == 'A':
        if MyList[0] == SecretList[0]:
            Solve -= 1
        MyList[0] -= 1
    elif c == 'C':
        if MyList[1] == SecretList[1]:
            Solve -= 1
        MyList[1] -= 1
    elif c == 'G':
        if MyList[2] == SecretList[2]:
            Solve -= 1
        MyList[2] -= 1
    elif c == 'T':
        if MyList[3] == SecretList[3]:
            Solve -= 1
        MyList[3] -= 1        
        
P, S = map(int, input().split())
A = input()
SecretList = list(map(int, input().split()))

for i in range(S):
    add_list(A[i])
    
for i in range(4):
    if SecretList[i] == 0:
        Solve += 1

if Solve == 4:
    Count += 1

for i in range(S, P):
    add_list(A[i])
    sub_list(A[i - S])
    if Solve == 4:
        Count += 1
        
print(Count)