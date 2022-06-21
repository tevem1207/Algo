import sys 
sys.stdin = open('input1.txt') 


from itertools import combinations
from collections import Counter


N, S = map(int, input().split())
arr = list(map(int, input().split()))
arr_1 = arr[:N//2]
arr_2 = arr[N//2:]
result_1 = []
result_2 = []
answer = 0

for i in range(1, N+1):
    result_1.extend(combinations(arr_1, i))
for i in range(1, N+1):
    result_2.extend(combinations(arr_2, i))

result_1 = sorted(map(sum, result_1))
result_2 = sorted(map(sum, result_2))
answer += sum([1 for x in result_1 + result_2 if x == S])
result_2 = Counter(result_2)

for num in result_1:
    if S - num in result_2:
        answer += result_2[S - num]

print(answer)
