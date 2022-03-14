import sys
sys.stdin = open('input.txt')

import heapq

N = int(input())
time = total = 0
people = list(map(int, input().split()))
heapq.heapify(people)

for _ in range(N):
    time += heapq.heappop(people)
    total += time

print(total)
