import sys
sys.stdin = open('input.txt')


def get_multiple(a, b):
    result = [[0, 0], [0, 0]]
    result[0][0] = (a[0][0]*b[0][0] + a[0][1]*b[1][0]) % 1000000007
    result[0][1] = (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % 1000000007
    result[1][0] = (a[1][0]*b[0][0] + a[1][1]*b[1][0]) % 1000000007
    result[1][1] = (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % 1000000007
    return result


def power(matrix, n):
    if n == 0:
        return [[1, 0], [0, 1]]

    x = power(matrix, n//2)

    if n % 2:
        return get_multiple(get_multiple(x, x), matrix)
    else:
        return get_multiple(x, x)


N = int(input())
fibo = [[1, 1], [1, 0]]

print(power(fibo, N)[0][1])
