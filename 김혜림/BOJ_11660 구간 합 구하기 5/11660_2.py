import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (N+1) for _ in range(N+1)]
to_find = [list(map(int, input().split())) for _ in range(M)]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]

for f in to_find:
    x1, y1, x2, y2 = f[0], f[1], f[2], f[3]

    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])

