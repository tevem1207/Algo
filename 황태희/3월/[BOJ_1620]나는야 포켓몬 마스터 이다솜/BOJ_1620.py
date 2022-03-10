import heapq, sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())

dogam = {}

for i in range(1, N+1):
    name = input().rstrip('\n')
    dogam[str(i)] = name
    dogam[name] = i

for _ in range(M):
    key = input().rstrip('\n')
    print(dogam[key])
