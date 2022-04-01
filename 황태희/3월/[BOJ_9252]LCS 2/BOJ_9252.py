import sys
sys.stdin = open('input.txt')


str1 = input()
str2 = input()

d = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]

for i in range(1, len(str2)+1):
    for j in range(1, len(str1)+1):
        if str1[j-1] == str2[i-1]:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = max(d[i-1][j], d[i][j-1])

print(d[-1][-1])

answer = ''
i, j = len(str2), len(str1)

while d[i][j]:
    tmp = 1
    for next_i, next_j in [(i-1, j), (i, j-1)]:
        if d[next_i][next_j] == d[i][j]:
            i, j = next_i, next_j
            tmp = 0
            break
    if tmp:
        answer = str1[j-1] + answer
        i, j = i-1, j-1

print(answer)
