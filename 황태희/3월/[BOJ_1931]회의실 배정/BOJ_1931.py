import sys

sys.stdin = open('input.txt')

import heapq, sys


input = sys.stdin.readline
N = int(input())
my_heap = []
now = 0
cnt = 0
for _ in range(N):
    s, e = map(int, input().split())
    heapq.heappush(my_heap, (e, s))

while my_heap:
    end, start = heapq.heappop(my_heap)
    if start >= now:
        now = end
        cnt += 1

print(cnt)