import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())

coins = []
answer = 0

for _ in range(N):
    coins.append(int(input()))

for i in range(N-1, -1, -1):
    answer += K // coins[i]
    K %= coins[i]
    if K == 0:
        print(answer)
        break
