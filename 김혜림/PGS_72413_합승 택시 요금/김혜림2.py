import heapq


def solution(n, s, a, b, fares):
    INF = float('inf')

    adjL = [[] for _ in range(n + 1)]
    for x, y, charge in fares:
        adjL[x].append((charge, y))
        adjL[y].append((charge, x))
    
    def dijkstra(start):
        distances = [INF] * (n+1)
        distances[start] = 0
        to_go = []
        heapq.heappush(to_go, (0, start))
        
        while to_go:
            fare, current = heapq.heappop(to_go)
            if distances[current] < fare:
                continue
            
            for f, v in adjL[current]:
                nextf = fare + f
                if nextf < distances[v]:
                    distances[v] = nextf
                    heapq.heappush(to_go, (nextf, v))
        return distances
    
    dp = [[]] + [dijkstra(i) for i in range(1, n+1)]
    answer = INF
    for i in range(1, n+1):
        answer = min(answer, dp[i][a] + dp[i][b] + dp[i][s])
    
    return answer
                
    
n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

print(solution(n, s, a, b, fares))