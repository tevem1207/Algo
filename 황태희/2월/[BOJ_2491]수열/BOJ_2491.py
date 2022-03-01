import sys
sys.stdin = open('input1.txt')

N = int(input())

arr = list(map(int, input().split()))

answer = []

tmp = arr[0]
up = down = 0

for num in arr[1:]:
    if num > tmp:
        up += 1
        answer.append(down)
        down = 0

    elif num < tmp:
        down += 1
        answer.append(up)
        up = 0

    else:
        up += 1
        down += 1

    tmp = num

answer.append(up)
answer.append(down)

print(max(answer)+1)