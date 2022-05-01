import sys
sys.stdin = open('input.txt')


def find_min_cost(ci, visitj, ssum, prej):
    global min_cost, arr, jlst
    # 0. 가지치기 
    if ssum >= min_cost:
        return
    
    # 1. 종료조건
    if ci >= N:
        if ssum < min_cost:
            min_cost = ssum
        return
    
    # 2. 이동
    for j in range(len(visitj)):
        # 2-1. 첫 집의 색깔 고르기
        if prej == -1:
            find_min_cost(ci + 1, visitj[:j] + visitj[j + 1:], ssum + arr[ci][visitj[j]], j)
        else:
            find_min_cost(ci+1, jlst[:visitj[j]]+jlst[visitj[j]+1:], ssum+arr[ci][visitj[j]], visitj[j])


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_cost = float('inf')
jlst = list(range(3))
find_min_cost(0, jlst, 0, -1)
print(min_cost)