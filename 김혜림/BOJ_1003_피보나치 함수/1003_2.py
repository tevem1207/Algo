import sys
sys.stdin = open('input2.txt')


def fibo(N):
    cnt = [
        [1, 0],
        [0, 1],
        [1, 1],
    ]
    
    for n in range(3, N+1):
        a = cnt[n-1][0] + cnt[n-2][0]
        b = cnt[n-1][1] + cnt[n-2][1]
        cnt.append([a, b])
    
    return cnt[N]


T = int(input())

for _ in range(T):
    N = int(input())
    print(*fibo(N))