import sys
sys.stdin = open('input1.txt')

import sys
N = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(N)]
for i in range(1, N):
    dp[i] = dp[i-1] + 1 if arr[i] < arr[i-1] else dp[i-1]
Q = int(input())
for _ in range(Q):
    x, y = map(int, sys.stdin.readline().split())
    print(dp[y-1]-dp[x-1])
