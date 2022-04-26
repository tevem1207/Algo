import heapq

def solution(n, s, a, b, fares):
    graph = [{} for _ in range(n+1)]
    d = [[float('inf') for _ in range(n+1)] for _ in range(3)]
    sab = [s, a, b]
    
    for fare in fares:
        graph[fare[0]][fare[1]] = fare[2]
        graph[fare[1]][fare[0]] = fare[2]
        
    for i in range(3):
        q = [(0, sab[i])]
        d[i][sab[i]] = 0
        while q:
            total, node = heapq.heappop(q)
            for next_node, fee in graph[node].items():
                next_total = total + fee
                if d[i][next_node] > next_total:
                    heapq.heappush(q, (next_total, next_node))
                    d[i][next_node] = next_total
    
    answer = float('inf')
    
    for j in range(1, n+1):
        total = 0
        for i in range(3):
            total += d[i][j]
        if total  < answer:
            answer = total       

    return answer