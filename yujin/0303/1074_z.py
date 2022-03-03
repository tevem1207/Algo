


def get_num(r,c):

    if r==0 and c==0:
        return 0
    elif r==0 and c==1:
        return 1
    elif r==1 and c==0:
        return 2
    elif r==1 and c==1:
        return 3
    else:
        return 2*(r % 2)+(c % 2) + get_num(r//2, c//2) * 4

N, r, c = map(int,input().split())
result = get_num(r,c)
print(f'{result}')