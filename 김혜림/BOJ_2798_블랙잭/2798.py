import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
cards = list(map(int, input().split()))

# 카드 중에 세장을 골라서 합이 M 이하 중 최대로 만들게 해야함.
max_total = 0
for i in range(2**N):
    subset = []
    for j in range(N):
        if i & (1 << j):
            subset.append(cards[j])
    if len(subset) == 3 and max_total < sum(subset) <= M:
        max_total = sum(subset)
print(max_total)
            
        