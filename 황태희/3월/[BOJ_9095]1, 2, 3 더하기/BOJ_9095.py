import sys
sys.stdin = open('input.txt')


def solution(N):
    dp = [0, 1, 2, 4]
    for n in range(4, N+1):
        dp.append(dp[n-1] + dp[n-2] + dp[n-3])
    return dp[N]


T = int(input())

for tc in range(T):
    N = int(input())
    print(solution(N))
