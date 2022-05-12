import sys 
sys.stdin = open('input1.txt') 

N, K = map(int, input().split())
S = list(map(lambda x: int(x) % 2, input().split()))
a = b = 0
tmp = max_len = 0

print(S)