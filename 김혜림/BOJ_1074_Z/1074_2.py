import sys
sys.stdin = open('input.txt')


def find_order(N, r, c):
    
    if not N:
        return 0
    
    else:
        # 1사분면
        if 0 <= r < 2**(N-1) and 0 <= c < 2**(N-1):
            return find_order(N-1, r, c)
            
        # 2사분면 
        elif 0 <= r < 2**(N - 1) <= c < 2**N:
            return 2**(2*N-2) + find_order(N - 1, r, c-2**(N - 1))
        
        # 3사분면
        elif 0 <= c < 2**(N - 1) <= r < 2**N:
            return 2 * 2 ** (2 * N - 2) + find_order(N - 1, r-2**(N - 1), c)
        
        # 4사분면
        else:
            return 3 * 2 ** (2 * N - 2) + find_order(N - 1, r-2**(N - 1), c-2**(N - 1))
    

T = int(input())

for _ in range(T):
    N, r, c = map(int, input().split())
    result = find_order(N, r, c)
    print(result)
    