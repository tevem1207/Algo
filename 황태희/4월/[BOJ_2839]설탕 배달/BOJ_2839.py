import sys 
sys.stdin = open('input4.txt')

N = int(input())
dp = [float('inf') for _ in range(5001)]
dp[3] = dp[5] = 1

for i in range(6, 5001):
    dp[i] = min(dp[i-3], dp[i-5]) + 1

if dp[N] == float('inf'):
    print(-1)
else:
    print(dp[N])