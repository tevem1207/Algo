import sys
sys.stdin = open('input.txt')


def solution(num):
    cnt = 1
    while num > start:
        if num % 2:
            if num % 10 == 1:
                num //= 10
            else:
                break
        else:
            num //= 2
        cnt += 1

    if num == start:
        return cnt
    else:
        return -1


start, end = map(int, input().split())

print(solution(end))
