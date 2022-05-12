import sys 
sys.stdin = open('input1.txt') 


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for n in range(1, N+1):
    for m in range(1, M+1):
        dp[n][m] = dp[n][m-1] + dp[n-1][m] + matrix[n-1][m-1] - dp[n-1][m-1]

result = -float('inf')

for n1 in range(N+1):
    for m1 in range(M+1):
        for n2 in range(n1+1, N+1):
            for m2 in range(m1+1, M+1):
                result = max(result, dp[n2][m2] - dp[n1][m2] - dp[n2][m1] + dp[n1][m1])

print(result)
