import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())

up = 1
down = 1
for i in range(m):
    up *= n - i
    down *= m - i

print(up//down)
