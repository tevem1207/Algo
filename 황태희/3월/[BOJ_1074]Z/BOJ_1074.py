import sys
sys.stdin = open('input.txt')

Z = [[0, 1], [2, 3]]

N, r, c = map(int, input().split())
answer = 0
while N:
    x, y = c//(2**(N-1)), r//(2**(N-1))
    answer += Z[y][x] * (2**(2*(N-1)))
    N -= 1
    r, c = r-y*2**N, c-x*2**N

print(answer)
