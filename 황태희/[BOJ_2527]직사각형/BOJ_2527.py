for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    if (x1, y1) == (p2, q2) or (p1, y1) == (x2, q2) or (p1, q1) == (x2, y2) or (x1, q1) == (q2, y2):
        print('c')

    elif p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:
        print('d')

    elif x1 == p2 or p1 == x2 or y1 == q2 or q1 == y2:
        print('b')

    else:
        print('a')
