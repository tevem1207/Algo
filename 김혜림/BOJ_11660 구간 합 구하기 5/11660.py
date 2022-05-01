import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
to_find = [list(map(int, input().split())) for _ in range(M)]


for f in to_find:
    ans = 0
    x1, y1, x2, y2 = f[0]-1, f[1]-1, f[2]-1, f[3]-1
    dx = x2-x1
    dy = y2-y1
    
    if x1 == x2 and y1 == y2:
        ans = arr[x1][y1]
    else:    
        for i in range(dx+1):
            for j in range(dy+1):
                ans += arr[x1+i][y1+j]
    print(ans)
        
    