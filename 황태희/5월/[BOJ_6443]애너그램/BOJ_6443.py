import sys 
sys.stdin = open('input1.txt') 

import sys


def dfs(answer):
    if len(answer) == len(input_str):
        answers.append(answer)

    for b in strs:
        if strs[b] > 0:
            strs[b] -= 1
            dfs(answer + b)
            strs[b] += 1


N = int(input())
for _ in range(N):
    input_str = sys.stdin.readline().strip()
    strs = {}
    for a in sorted(input_str):
        if a in strs:
            strs[a] += 1
        else:
            strs[a] = 1

    answers = []
    for b in strs:
        strs[b] -= 1
        dfs(b)
        strs[b] += 1

    for answer in answers:
        print(answer)
