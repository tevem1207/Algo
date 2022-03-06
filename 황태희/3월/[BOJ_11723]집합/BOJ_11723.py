import sys
sys.stdin = open('input.txt')

import sys

input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    cal = input().rstrip()
    if cal == 'all':
        S = set(range(1, 21))
    elif cal == 'empty':
        S = set()
    else:
        N = int(cal.split()[1])
        if 'add' in cal:
            S |= {N}
        elif 'remove' in cal:
            S -= {N}
        elif 'check' in cal:
            if N in S:
                print(1)
            else:
                print(0)
        else:
            if N in S:
                S ^= {N}
            else:
                S |= {N}
