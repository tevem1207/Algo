import sys 
sys.stdin = open('input1.txt')

T = int(input())

for tc in range(T):
    matrix = [[], []]
    N = int(input())
    for i in range(2):
        matrix[i] = [0] + list(map(int, input().split()))
    dp = [[0 for _ in range(N+1)] for _ in range(2)]
    for i in range(1, N+1):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + matrix[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + matrix[1][i]

    if N == 1:
        print(max(matrix[0][1], matrix[1][1]))
    else:
        print(max(dp[0][-1], dp[1][-1]))
