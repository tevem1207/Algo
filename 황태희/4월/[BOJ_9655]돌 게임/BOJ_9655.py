import sys 
sys.stdin = open('input1.txt')

N = int(input())
dp = [float('inf') for _ in range(1001)]
dp[3] = dp[1] = 1
dp[2] = 2

for i in range(4, 1001):
    dp[i] = min(dp[i-3], dp[i-1]) + 1

if dp[N] % 2:
    print('SK')
else:
    print('CY')
