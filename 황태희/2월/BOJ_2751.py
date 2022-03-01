import heapq

N = int(input())

numbers = []

for _ in range(N):
    heapq.heappush(numbers, int(input()))
    
for _ in range(N):
    print(heapq.heappop(numbers))