import sys
sys.stdin = open('input.txt')

import sys, heapq


input = sys.stdin.readline

T = int(input())
for tc in range(T):
    K = int(input())
    Q = {}
    max_Q = []
    min_Q = []
    EMPTY = 0
    answer = []
    for _ in range(K):
        cal, N = input().split()
        N = int(N)
        if cal == 'I':
            heapq.heappush(max_Q, -N)
            heapq.heappush(min_Q, N)
            if N in Q:
                Q[N] += 1
            else:
                Q[N] = 0
        elif Q:
            if N == 1:
                num = -heapq.heappop(max_Q)
                while num not in Q:
                    if not max_Q:
                        print('EMPTY')
                        EMPTY = 1
                        break
                    num = -heapq.heappop(max_Q)
                else:
                    if Q[num]:
                        Q[num] -= 1
                    else:
                        Q.pop(num)
            else:
                num = heapq.heappop(min_Q)
                while num not in Q:
                    if not min_Q:
                        print('EMPTY')
                        EMPTY = 1
                        break
                    num = heapq.heappop(min_Q)
                else:
                    if Q[num]:
                        Q[num] -= 1
                    else:
                        Q.pop(num)

    if not EMPTY:
        num = -heapq.heappop(max_Q)
        while num not in Q:
            if not max_Q:
                print('EMPTY')
                EMPTY = 1
                break
            num = -heapq.heappop(max_Q)
        else:
            answer.append(num)
        if not EMPTY:
            num = heapq.heappop(min_Q)
            while num not in Q:
                if not min_Q:
                    print('EMPTY')
                    EMPTY = 1
                    break
                num = heapq.heappop(min_Q)
            else:
                answer.append(num)
                print(*answer)
