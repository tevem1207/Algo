import sys
sys.stdin = open('input.txt')


from collections import deque


def drop(index):
    matrix[0][index] = n
    t_matrix = list(zip(*matrix))
    matrix[0][index] = 0

    for i in range(7):
        tmp = deque()
        for num in t_matrix[i]:
            if num:
                tmp.append(num)
        while len(tmp) < 7:
            tmp.appendleft(0)
        t_matrix[i] = tmp

    result = list(zip(*t_matrix))
    for i in range(7):
        result[i] = list(result[i])

    return result


def solution(input_matrix):
    matrix2 = [[0 for _ in range(7)] for _ in range(7)]
    matrix3 = [[0 for _ in range(7)] for _ in range(7)]

    for i in range(7):
        for j in range(7):
            if input_matrix[i][j]:
                matrix2[i][j] = 1

    for i in range(1, 7):
        for j in range(1, 7):
            if input_matrix[i][j]:
                matrix2[i][j] = matrix2[i][j-1] + 1

    for i in range(7):
        for j in range(6)[::-1]:
            if input_matrix[i][j] and input_matrix[i][j+1]:
                matrix2[i][j] = matrix2[i][j+1]

    for j in range(7):
        for i in range(7):
            if input_matrix[i][j]:
                matrix3[i][j] = 1

    for j in range(7):
        for i in range(1, 7):
            if input_matrix[i][j]:
                matrix3[i][j] = matrix3[i-1][j] + 1

    for j in range(7):
        for i in range(6)[::-1]:
            if matrix3[i][j] and matrix3[i+1][j]:
                matrix3[i][j] = matrix3[i+1][j]

    for i in range(7):
        for j in range(7):
            if input_matrix[i][j]:
                if input_matrix[i][j] == matrix2[i][j] or input_matrix[i][j] == matrix3[i][j]:
                    input_matrix[i][j] = 0

    t_matrix = list(zip(*input_matrix))

    for i in range(7):
        tmp = deque()
        for num in t_matrix[i]:
            if num:
                tmp.append(num)
        while len(tmp) < 7:
            tmp.appendleft(0)
        t_matrix[i] = tmp

    result = list(zip(*t_matrix))
    for i in range(7):
        result[i] = list(result[i])
    return result


matrix = [list(map(int, input().split())) for _ in range(7)]

n = int(input())

answer = float('inf')

for k in range(7):
    new_matrix = drop(k)

    tmp = [new_matrix[i][::] for i in range(7)]
    now = solution(new_matrix)

    while now != tmp:
        tmp = [now[i][::] for i in range(7)]
        now = solution(now)

    total = 0

    for i in range(7):
        for j in range(7):
            if now[i][j]:
                total += 1

    answer = min(total, answer)

print(answer)
