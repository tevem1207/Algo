import sys
sys.stdin = open('input.txt')


K = int(input())
L = 8
width = height = 0
arr = []
idx = [0, 0]
answer = 0

for i in range(6):
    D, N = map(int, input().split())
    arr.append((D, N))
    if D == 1 or D == 2:
        if N > width:
            width = N
            idx[0] = i
    else:
        if N > height:
            height = N
            idx[1] = i

answer += width * height

width = height = 0

if idx == [0, 5] or idx == [5, 0]:
    width = arr[2][1]
    height = arr[3][1]

else:
    width = arr[(max(idx)+2) % 6][1]
    height = arr[(max(idx)+3) % 6][1]

answer -= width * height
answer *= K

print(answer)
