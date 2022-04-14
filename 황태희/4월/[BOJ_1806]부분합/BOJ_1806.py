import sys 
sys.stdin = open('input1.txt')

N, S = map(int, input().split())

arr = list(map(int, input().split()))
start, end = 0, 0
total = arr[start]
answer = float('inf')

while end < N:
    if total < S:
        if end < N-1:
            end += 1
            total += arr[end]
        else:
            break

    elif total >= S:
        answer = min(answer, end - start + 1)
        total -= arr[start]
        start += 1

if answer == float('inf'):
    print(0)
else:
    print(answer)
