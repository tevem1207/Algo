import sys 
sys.stdin = open('input.txt') 

n = int(input())

arr = sorted(list(map(int, input().split())))
start, end = 0, n-1
answer = [float('inf'), 0, 0]

while start < end:
    tmp = arr[start] + arr[end]
    if tmp == 0:
        answer = [tmp, arr[start], arr[end]]
        break
    elif abs(tmp) < answer[0]:
        answer = [abs(tmp), arr[start], arr[end]]
    if tmp > 0:
        end -= 1
    elif tmp < 0:
        start += 1

print(answer[1], answer[2])
