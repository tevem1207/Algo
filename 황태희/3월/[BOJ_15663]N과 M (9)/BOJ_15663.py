import sys
sys.stdin = open('input.txt')


from itertools import permutations


N, M = map(int, input().split())
arr = sorted(map(int, input().split()))

for answer in sorted(list(set(permutations(arr, M)))):
    print(*answer)
