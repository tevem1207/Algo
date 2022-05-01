# 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find_combi(idx, ssum, cnt):
    global min_diff, min_cnt
    # 부분합 생성
    while idx + 1 <= N:
        if ssum >= S or idx == N-1: 
            if ssum - S < min_diff:
                min_diff = ssum - S
                min_cnt = cnt
            return
        idx += 1
        ssum += numbers[idx]
        cnt += 1
    return


N, S = map(int, input().split())
numbers = list(map(int, input().split()))

min_diff = float('inf')
min_cnt = 0
for i in range(N):
    if numbers[i] == S:
        min_cnt = 1
        break
    else:
        find_combi(i, numbers[i], 1)

print(min_cnt)    

