import sys
sys.stdin = open('input.txt')

match = (5, 3, 4, 1, 2, 0)

N = int(input())
dices = []
for _ in range(N):
    dices.append(list(map(int, input().split())))

answer = 0
for i in range(6):
    idx = i
    num = dices[0][idx]
    tmp = 0

    for dice in dices:
        idx = match[dice.index(num)]
        if num == 6 or dice[idx] == 6:
            if num == 5 or dice[idx] == 5:
                tmp += 4
            else:
                tmp += 5
        else:
            tmp += 6
        num = dice[idx]

    if tmp > answer:
        answer = tmp

print(answer)