# 투포인터 풀이!!
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

s = e = 0
min_cnt = float('inf')
tmp_ssum = numbers[s]
while True:
    if e == N-1 and tmp_ssum < S:
        break
    if tmp_ssum < S and e < N-1:
        e += 1
        tmp_ssum += numbers[e]
    if tmp_ssum >= S:
        if e-s+1 < min_cnt:
            min_cnt = e-s+1
        tmp_ssum -= numbers[s]
        s += 1

print(0) if min_cnt == float('inf') else print(min_cnt)