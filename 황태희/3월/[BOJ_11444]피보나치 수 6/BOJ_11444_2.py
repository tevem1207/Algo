import sys
sys.stdin = open('input.txt')


def get_multiple(a, b):
    result = [[0, 0], [0, 0]]
    result[0][0] = (a[0][0]*b[0][0] + a[0][1]*b[1][0]) % 1000000007
    result[0][1] = (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % 1000000007
    result[1][0] = (a[1][0]*b[0][0] + a[1][1]*b[1][0]) % 1000000007
    result[1][1] = (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % 1000000007
    return result


N = int(input())
fibo = [[1, 1], [1, 0]]
odds = []

while N != 1:
    if N % 2:
        odds.append(fibo)
    fibo = get_multiple(fibo, fibo)
    N //= 2

while odds:
    odd = odds.pop()
    fibo = get_multiple(fibo, odd)

print(fibo[0][1])
