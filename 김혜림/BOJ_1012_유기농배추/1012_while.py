import sys
sys.stdin = open("input.txt")


def dfs(n, m):
    to_visit = [(n, m)]
    while to_visit:
        cn, cm = to_visit.pop()
        if not visited[cn][cm]:
            visited[cn][cm] = True
   
            for dn, dm in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                n = cn + dn
                m = cm + dm
                if 0 <= n < N and 0 <= m < M and matrix[n][m] and not visited[n][m]:
                    to_visit.append((n, m))
    

def get_area_num():
    area = 0
    for cabbage in cabbages:
        n, m = cabbage[0], cabbage[1]
        if not visited[n][m]:
            area += 1
            dfs(n, m)
                    
    return area
    

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    
    matrix = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    
    cabbages = []
    for _ in range(K):
        j, i = map(int, input().split())
        matrix[i][j] = 1
        cabbages.append((i, j))
    
    print(get_area_num())