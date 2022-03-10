import sys
sys.stdin = open('input2.txt')


def fibo(N):
    global cnt0, cnt1
    if N == 0:
        cnt0 += 1
        return 0
    elif N == 1:
        cnt1 += 1
        return 1
    else: 
        return fibo(N-1) + fibo(N-2)
    
    
T = int(input())

for _ in range(T):
    cnt0 = 0
    cnt1 = 0
    N = int(input())
    fibo(N)
    print(f'{cnt0} {cnt1}')