import sys 
sys.stdin = open('input6.txt')


N = int(input())
input_str = '0' + input()
get_next = {'B': 'O', 'O': 'J', 'J': 'B'}

dp = [float('inf') for _ in range(N+1)]
dp[1] = 0

for i in range(1, N+1):
    for j in range(i+1, N+1):
        if input_str[j] == get_next[input_str[i]]:
            dp[j] = min(dp[j], dp[i] + (j-i)**2)

if dp[N] == float('inf'):
    print(-1)
else:
    print(dp[N])
