import sys
sys.stdin = open('input.txt')


def blow_sand(d):
    x, y = now[0], now[1]
    sand = matrix[y][x]
    matrix[y][x] = 0
    out = 0
    # 7%
    if 0 <= x + delta[(d+1)%4][0] < N and 0 <= y + delta[(d+1)%4][1] < N:
        matrix[y + delta[(d+1)%4][1]][x + delta[(d+1)%4][0]] += int(sand*7/100)
    else:
        out += int(sand*7/100)
    if 0 <= x + delta[(d+3)%4][0] < N and 0 <= y + delta[(d+3)%4][1] < N:
        matrix[y + delta[(d+3)%4][1]][x + delta[(d+3)%4][0]] += int(sand*7/100)
    else:
        out += int(sand*7/100)

    # 2%
    if 0 <= x + 2*delta[(d+1)%4][0] < N and 0 <= y + 2*delta[(d+1)%4][1] < N:
        matrix[y + 2*delta[(d+1)%4][1]][x + 2*delta[(d+1)%4][0]] += int(sand*2/100)
    else:
        out += int(sand*2/100)
    if 0 <= x + 2*delta[(d+3)%4][0] < N and 0 <= y + 2*delta[(d+3)%4][1] < N:
        matrix[y + 2*delta[(d+3)%4][1]][x + 2*delta[(d+3)%4][0]] += int(sand*2/100)
    else:
        out += int(sand*2/100)

    # 10%
    if 0 <= x + delta[(d+1)%4][0] + delta[d][0] < N and 0 <= y + delta[(d+1)%4][1] + delta[d][1] < N:
        matrix[y + delta[(d+1)%4][1] + delta[d][1]][x + delta[(d+1)%4][0] + delta[d][0]] += int(sand * 10 / 100)
    else:
        out += int(sand * 10 / 100)
    if 0 <= x + delta[(d+3)%4][0] + delta[d][0] < N and 0 <= y + delta[(d+3)%4][1] + delta[d][1] < N:
        matrix[y + delta[(d+3)%4][1] + delta[d][1]][x + delta[(d+3)%4][0] + delta[d][0]] += int(sand * 10 / 100)
    else:
        out += int(sand * 10 / 100)

    # 1%
    if 0 <= x + delta[(d+1)%4][0] - delta[d][0] < N and 0 <= y + delta[(d+1)%4][1] - delta[d][1] < N:
        matrix[y + delta[(d+1)%4][1] - delta[d][1]][x + delta[(d+1)%4][0] - delta[d][0]] += int(sand * 1 / 100)
    else:
        out += int(sand * 1 / 100)
    if 0 <= x + delta[(d+3)%4][0] - delta[d][0] < N and 0 <= y + delta[(d+3)%4][1] - delta[d][1] < N:
        matrix[y + delta[(d+3)%4][1] - delta[d][1]][x + delta[(d+3)%4][0] - delta[d][0]] += int(sand * 1 / 100)
    else:
        out += int(sand * 1 / 100)

    # 5%
    if 0 <= x + 2*delta[d][0] < N and 0 <= y + 2*delta[d][1] < N:
        matrix[y + 2*delta[d][1]][x + 2*delta[d][0]] += int(sand * 5 / 100)
    else:
        out += int(sand * 5 / 100)

    # alpha
    sand -= (2 * int(sand*7/100)) + (2 * int(sand*2/100)) + \
            (2 * int(sand * 10 / 100)) + (2 * int(sand * 1 / 100)) + int(sand * 5 / 100)

    if 0 <= x + delta[d][0] < N and 0 <= y + delta[d][1] < N:
        matrix[y + delta[d][1]][x + delta[d][0]] += sand
    else:
        out += sand
    return out


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

now = [N//2, N//2]
cnt = 0
m = 1
answer = 0

while now != [N-1, 0]:
    for _ in range(2):
        for _ in range(m):
            now[0], now[1] = now[0] + delta[cnt][0], now[1] + delta[cnt][1]
            answer += blow_sand(cnt)
        cnt = (cnt + 1) % 4
    m += 1

for _ in range(N-1):
    now[0], now[1] = now[0] + delta[0][0], now[1] + delta[0][1]
    answer += blow_sand(cnt)

print(answer)
