import sys
sys.stdin = open('input.txt')


def go_z(N, i, j):
    global cnt
    # 0. base 가장 작은 단계 일때,
    if N == 1:
        # 델타 이동
        for di, dj in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            cnt += 1
            if i+di == r and j+dj == c:
                print(cnt)
                return cnt
    
    # 1. 그 이후부터 4등분이 되어 있다는 것이 핵심
    else:
        # go_z가 실행될 시작점 
        for x, y in [(0, 0), (0, 2**(N-1)), (2**(N-1), 0), (2**(N-1), 2**(N-1))]:
            # 조건 하나 추가 cnt로 플래그써보자! 
            go_z(N-1, x, y)
            # 제대로 찾아서 return 값이 있다면 더이상 재귀 반복 안해도 된다.
        
                       
T = int(input())

for _ in range(T):
    N, r, c = map(int, input().split())
    cnt = -1
    go_z(N, 0, 0)
    
    