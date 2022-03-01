import sys
sys.stdin = open('input3.txt')


def assign_seats(matrix):
    i, j = Y, 0
    n = 1
    
    while not matrix[i-1][j] and n <= X*Y:
        # 상 우 하 좌 순
        for di, dj in [(-1, 0),  (0, 1), (1, 0), (0, -1)]:
            while 0 <= (i+di) < Y and 0 <= (j+dj) < X and not matrix[i+di][j+dj]:
                ni = i + di
                nj = j + dj
                matrix[ni][nj] = n
                if n == N:
                    return (nj+1, Y-ni)
                else:
                    n += 1
                    i, j = ni, nj
    
    
X, Y = map(int, input().split())
N = int(input())
matrix = [[0]*X for _ in range(Y)]

if N > X * Y:
    print(0)
else:
    ans = assign_seats(matrix)
    print(*ans)
