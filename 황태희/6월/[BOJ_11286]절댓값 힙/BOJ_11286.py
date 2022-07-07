import sys
sys.stdin = open(f'input{1}.txt')

import heapq
import sys


N = int(input())
q = []

for _ in range(N):
    x = int(sys.stdin.readline())
    heapq.heappush(q, (abs(x), x)) if x else (print(heapq.heappop(q)[1]) if q else print(0))
