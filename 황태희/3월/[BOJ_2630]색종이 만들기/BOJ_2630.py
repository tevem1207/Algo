import sys
sys.stdin = open('input.txt')


def cut_paper(x, y, n):
    global white
    global blue

    if n == 1:
        if matrix[y][x]:
            blue += 1
        else:
            white += 1
        return

    total = 0
    for i in range(n):
        total += sum(matrix[y+i][x:x+n])
    if total == 0:
        white += 1
    elif total == n**2:
        blue += 1
    else:
        for next_x, next_y in [(x, y), (x+n//2, y), (x, y+n//2), (x+n//2, y+n//2)]:
            cut_paper(next_x, next_y, n//2)


N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]
white = blue = 0

cut_paper(0, 0, N)

print(white)
print(blue)
