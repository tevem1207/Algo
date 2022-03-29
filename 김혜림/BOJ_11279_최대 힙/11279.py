# 자연수가 입력되면 넣고, 0이라면 pop
import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

max_heap = []
N = int(input())
for _ in range(N):
    x = int(input())

    if x == 0:
        if not max_heap:
            print(0)
        else:
            a = heapq.heappop(max_heap)
            max_heap.pop()
            print(-a)
    else:
        heapq.heappush(max_heap, x)
        heapq.heappush(max_heap, -x)