# 중복없이 M개를 골라서 오름차순으로 만들기
# 중복되는 수열을 여러 번 출력하면 X
import sys
from itertools import combinations
sys.stdin = open('input.txt')

N, M = map(int, input().split())
numbers = list(range(1, N+1))

seq = list(combinations(numbers, M))
for s in seq:
    print(*s)
