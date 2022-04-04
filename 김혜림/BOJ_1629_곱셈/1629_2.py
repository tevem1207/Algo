import sys
sys.stdin = open("input.txt")

def power(A, B):
    ret = 1
    while B > 0:
        if B % 2 != 0:
            ret *= A
        A *= A
        B //= 2
    return ret    


A, B, C = map(int, input().split())
print(power(A, B) % C)