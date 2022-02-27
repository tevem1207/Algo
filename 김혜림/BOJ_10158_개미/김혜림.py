import sys
sys.stdin = open('input2.txt')


def move(p, q):
    # p q를 그대로 x y 축으로 생각해보자
    x, y = p, q
    t = 0

    while t < T:
        for dx, dy in [(1, 1), (-1, 1), (-1, -1), (-1, 1)]:
            # 갈 수 있는 길이면 계속 그 방향으로 이동, 한시간 추가
            while 0 <= (x+dx) <= w and 0 <= (y+dy) <= h:
                x += dx 
                y += dy
                t += 1
                if t == T:
                    return x, y


w, h = map(int, input().split())
p, q = map(int, input().split())
T = int(input())

ans = move(p, q)
print(*ans)