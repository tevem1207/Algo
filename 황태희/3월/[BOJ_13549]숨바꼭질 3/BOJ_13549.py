import heapq


def find_k():
    while Q:
        time, now_position = heapq.heappop(Q)
        for next_time, next_position in [(time, now_position*2), (time+1, now_position+1), (time+1, now_position-1)]:
            if next_position == K:
                return next_time

            if 0 <= next_position <= 100000 and not visited[next_position]:
                heapq.heappush(Q, [next_time, next_position])
                visited[next_position] = True
                d[next_position] = next_time


N, K = map(int, input().split())

d = [100000 for _ in range(100001)]
visited = [False for _ in range(100001)]
d[N] = 0
visited[N] = True
Q = [[0, N]]

if N >= K:
    print(N - K)
else:
    print(find_k())
