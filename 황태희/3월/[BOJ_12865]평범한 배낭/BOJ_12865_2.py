import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())

arr = []

for _ in range(N):
    W, V = map(int, input().split())
    arr.append((W, V))

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if arr[i-1][0] <= j:
            dp[i][j] = max(arr[i-1][1] + dp[i-1][j - arr[i-1][0]], dp[i-1][j])

        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])