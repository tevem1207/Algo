import sys
sys.stdin = open('input.txt')


def power(num, n):
    if n == 0:
        return 1

    x = power(num, n//2)

    if n % 2:
        return (x * x * num) % C
    else:
        return (x * x) % C


A, B, C = map(int, input().split())

print(power(A, B))