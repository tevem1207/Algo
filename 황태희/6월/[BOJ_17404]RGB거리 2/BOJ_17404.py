import sys 
sys.stdin = open('input1.txt')


N = int(input())
rgb = []
ans = float('inf')

for _ in range(N):
    rgb.append(list(map(int, input().split())))

for i in range(3):
    dp = [[float('inf') for _ in range(3)] for _ in range(N)]
    dp[0][i] = rgb[0][i]
    for j in range(1, N):
        dp[j][0] = rgb[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = rgb[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = rgb[j][2] + min(dp[j-1][0], dp[j-1][1])

    for j in range(3):
        if i != j:
            ans = min(ans, dp[-1][j])

print(ans)