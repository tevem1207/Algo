import sys
sys.stdin = open('input.txt')


def is_group(str):
    tmp = str[0]
    strs = [tmp]

    for i in str[1:]:
        if i != tmp:
            if i in strs:
                return 0
            strs.append(i)
        tmp = i
    return 1


N = int(input())
answer = 0

for _ in range(N):
    answer += is_group(input())

print(answer)