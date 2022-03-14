import sys
sys.stdin = open("input.txt")


def dfs(n, m):
    visited[n][m] = True
    for dn, dm in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nn = n + dn
        nm = m + dm
        # 2. 갈 수 있는 길이면서
        if 0 <= nn < N and 0 <= nm < M and matrix[nn][nm]:
            # 2. 방문한 적이 없다면 이동
            if not visited[nn][nm]:
                dfs(nn, nm)
            


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