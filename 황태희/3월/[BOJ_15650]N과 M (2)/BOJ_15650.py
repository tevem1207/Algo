import sys
sys.stdin = open('input.txt')


from itertools import combinations


N, M = map(int, input().split())

for answer in combinations(range(1, 1+N), M):
    print(*answer)