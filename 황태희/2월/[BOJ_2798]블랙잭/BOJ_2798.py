import sys
sys.stdin = open('input.txt')


def get_blackjack(cards, N, M):
    blackjack = [0, M]
    tmp = [0, M]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if not (i == j or j == k or i == k):
                    tmp[0] = cards[i] + cards[j] + cards[k]
                    if tmp[0] <= M:
                        tmp[1] = M - tmp[0]
                        if not tmp[1]:
                            return tmp[0]
                        else:
                            if tmp[1] < blackjack[1]:
                                blackjack = tmp[:]
    return blackjack[0]


N, M = map(int, input().split())
cards = list(map(int, input().split()))
print(get_blackjack(cards, N, M))
