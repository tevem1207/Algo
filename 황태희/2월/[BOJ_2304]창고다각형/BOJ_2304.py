import sys
sys.stdin = open('input.txt')


N = int(input())
arr = []
idx_min = 1000
idx_max = 0

for _ in range(N):
    L, H = map(int, input().split())
    if L < idx_min:
        idx_min = L
    if L > idx_max:
        idx_max = L
    arr.append((L, H))

warehouse = [0 for _ in range(1001)]
arr.sort(key=lambda x: x[1])
maxes = [arr.pop()]

if arr:
    while arr[-1][1] >= maxes[0][1]:
        maxes.append(arr.pop())
        if not arr:
            break

maxes.sort()

for i in range(maxes[0][0], maxes[-1][0]+1):
    warehouse[i] = maxes[0][1]

L, R = maxes[0][0], maxes[-1][0]

while arr:

    idx, height = arr.pop()
    if idx < L:
        for i in range(idx, L):
            if warehouse[i] < height:
                warehouse[i] = height
        L = idx
    elif idx > R:
        for i in range(R+1, idx+1):
            if warehouse[i] < height:
                warehouse[i] = height
        idx = R

print(sum(warehouse))