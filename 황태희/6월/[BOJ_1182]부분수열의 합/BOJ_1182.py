import sys 
sys.stdin = open('input1.txt') 


from itertools import combinations


N, S = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
for i in range(1, N+1):
    answer += sum([1 for x in combinations(arr, i) if sum(x) == S])
print(answer)
