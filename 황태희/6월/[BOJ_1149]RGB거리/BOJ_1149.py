import sys 
sys.stdin = open('input5.txt')


N = int(input())
dp = [[0 for _ in range(N+1)] for _ in range(3)]

for i in range(1, N+1):
    R, G, B = map(int, input().split())
    dp[0][i] = min(dp[1][i - 1], dp[2][i - 1]) + R
    dp[1][i] = min(dp[0][i - 1], dp[2][i - 1]) + G
    dp[2][i] = min(dp[0][i - 1], dp[1][i - 1]) + B

print(min([dp[i][-1] for i in range(3)]))
