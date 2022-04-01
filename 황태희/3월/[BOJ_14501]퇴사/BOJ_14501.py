import sys
sys.stdin = open('input.txt')


N = int(input())
arr = []

for i in range(N):
    T, P = map(int, input().split())
    arr.append([T, P])

dp = [p for t, p in arr]

for i in range(len(dp)):
    max_d = 0
    for j in range(i):
        if arr[j][0] + j <= i:
            if max_d < dp[j]:
                max_d = dp[j]
    if i + arr[i][0] <= N:
        dp[i] = arr[i][1] + max_d
    else:
        dp[i] = max_d

print(max(dp))
