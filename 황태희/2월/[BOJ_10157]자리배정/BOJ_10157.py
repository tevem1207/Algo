import sys
sys.stdin = open('input.txt')


delta = [(1, 1), (-1, -1)]

C, R = map(int, input().split())

K = int(input())

x = y = 1
num = 1
M = C - 1
N = R - 1

if K > C*R:
    print(0)

else:
    while K >= num:
        for direction in range(2):
            dx, dy = delta[direction]
            y = y + dy * N
            num += N
            if K < num:
                print(x, y-(num - K)*dy)
                break

            x = x + dx * M
            num += M
            if K < num:
                print(x-(num - K)*dx, y)
                break
        M -= 2
        N -= 2
        x += 1
        y += 1

