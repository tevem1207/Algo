

def get_case(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    elif N == 3:
        return 4
    else:
        return get_case(N-3)+get_case(N-2)+get_case(N-1)


T = int(input())
for tc in range(1, T+1):
    num = int(input())
    print(f'{get_case(num)}')