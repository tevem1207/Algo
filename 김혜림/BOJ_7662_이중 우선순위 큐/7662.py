# 데이터를 삭제할 때 연산(operation) 명령에 따라 우선순위가 가장 높은 데이터 또는 가장 낮은 데이터 중 하나를 삭제하는 점이다. 
import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())  # 연산의 개수
    max_heap = []
    min_heap = []
    valid = [0 for _ in range(1000001)]

    for idx in range(k):
        oper, num = input().split()
        num = int(num)
        
        if oper == 'I':
            heapq.heappush(max_heap, (-num, idx))
            heapq.heappush(min_heap, (num, idx))
            valid[idx] = 1
        else:
            if len(min_heap) == 0:
                continue
            if num == 1:
                while max_heap and not valid[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    valid[heapq.heappop(max_heap)[1]] = 0
            else:
                while min_heap and not valid[min_heap[0][1]]:
                    heapq.heappop(min_heap)

                if min_heap:
                    valid[heapq.heappop(min_heap)[1]] = 0

    while max_heap and not valid[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not valid[min_heap[0][1]]:
        heapq.heappop(min_heap)
        
    if not max_heap and not min_heap:
        print("EMPTY")
    else:
        max_num = heapq.heappop(max_heap)[0] * -1
        min_num = heapq.heappop(min_heap)[0]
        print(f"{max_num} {min_num}")

    