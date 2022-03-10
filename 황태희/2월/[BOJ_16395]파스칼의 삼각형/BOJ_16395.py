import sys
sys.stdin = open('input.txt', encoding='UTF-8')


def get_pascal(N):
    if N == 1:
        return [[1]]

    cnt = 2
    pascal = [[1], [1, 1]]

    while cnt < N:
        tmp = [1]
        for i in range(1, cnt):
            tmp.append(pascal[-1][i]+pascal[-1][i-1])
        tmp.append(1)
        pascal.append(tmp)
        cnt += 1

    return pascal


N, K = map(int, input().split())
pascal = get_pascal(N)
print(pascal[N-1][K-1])
