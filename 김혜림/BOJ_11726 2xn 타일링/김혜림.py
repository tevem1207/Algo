import sys
sys.stdin = open('input.txt')


def get_pieces(n):
    memo = [0, 1, 2]

    if n in (1, 2):
        return memo[n]
    else:
        for i in range(3, n + 1):
            memo.append(memo[i - 1] + memo[i - 2])
        return memo[-1]


N = int(input())

print(get_pieces(N)%10007)