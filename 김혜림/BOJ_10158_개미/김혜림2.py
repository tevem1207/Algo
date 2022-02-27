import sys
sys.stdin = open('input1.txt')


def move(p, q):

    x = 2*w - (p + T) % (2*w) if (p + T) % (2*w) > w else (p + T) % (2*w)
    y = 2*h - (q + T) % (2*h) if (q + T) % (2*h) > h else (q + T) % (2*h)
    
    return x, y


w, h = map(int, input().split())
p, q = map(int, input().split())
T = int(input())

ans = move(p, q)
print(*ans)