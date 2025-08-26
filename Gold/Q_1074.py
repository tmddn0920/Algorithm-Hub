count = 0
N, r, c = map(int, input().split())

def visit(N, r, c):
    global count
    temp = 2**(N - 1)
    temp_r = r // temp
    temp_c = c // temp
    if temp_r == 0 and temp_c == 1:
        count += 1 * (temp**(2))
        c = c - temp
    elif temp_r == 1  and temp_c == 0:
        count += 2 * (temp**(2))
        r = r - temp
    elif temp_r == 1 and temp_c == 1:
        count += 3 * (temp**(2))
        c = c - temp
        r = r - temp
    N = N - 1
    if N >= 1:
        visit(N, r, c)
        
visit(N, r, c)
print(count)