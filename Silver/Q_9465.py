T = int(input())
for _ in range(T):
    N = int(input())
    up = list(map(int, input().split()))
    down = list(map(int, input().split()))
    
    dp_up = up[0]
    dp_down = down[0]
    dp_not = 0
    
    for i in range(1, N):
        ndp_up = max(dp_down, dp_not) + up[i]
        ndp_down = max(dp_up, dp_not) + down[i]
        ndp_not = max(dp_up, dp_down, dp_not)
        dp_up, dp_down, dp_not = ndp_up, ndp_down, ndp_not
        
    print(max(dp_up, dp_down, dp_not))