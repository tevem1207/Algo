import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T)
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    ssum = 0
    for j in range(N):
        if arr[0][j] >= arr[1][j]:
            