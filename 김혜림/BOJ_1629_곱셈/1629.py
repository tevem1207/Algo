import sys
sys.stdin = open("input.txt")


def power(A, B):
    global C
    if B == 0:
        return 1
    tmp = power(A%C, B//2) % C
    
    # 짝수인 경우
    if B % 2 == 0:
        return tmp * tmp
    # 홀수인 경우
    else:
        return tmp * tmp * A
    
    
A, B, C = map(int, input().split())
print(power(A, B) % C)