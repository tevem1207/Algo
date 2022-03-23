import sys
sys.stdin = open('input.txt')


from itertools import permutations


N, M = map(int, input().split())

for answer in permutations(range(1, 1+N), M):
    print(*answer)
