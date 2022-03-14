import sys
sys.stdin = open('input2.txt')


T = int(input())

for _ in range(T):
    N = int(input())
    fibo = [{0: 1, 1: 0}, {0: 0, 1: 1}]
    for n in range(2, N+1):
        fibo.append({0: fibo[n-1][0] + fibo[n-2][0], 1: fibo[n-1][1] + fibo[n-2][1]})

    print(fibo[N][0], fibo[N][1])
