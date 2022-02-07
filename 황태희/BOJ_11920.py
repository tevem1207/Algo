import heapq

N, K = map(int, input().split())
numbers = list(map(int, input().split()))

heap = []

for number in numbers:
    heapq.heappush(heap, number)
    if len(heap) > K:
        print(heapq.heappop(heap), end = ' ')
        
for _ in range(K):
    print(heapq.heappop(heap), end=' ')
