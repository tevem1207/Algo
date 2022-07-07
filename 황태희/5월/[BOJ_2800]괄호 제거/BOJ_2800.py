import sys 
sys.stdin = open('input1.txt')


from itertools import combinations


input_str = list(input().strip())
arr = list(enumerate(input_str))
result = []
stack = []

while arr:
    tmp = arr.pop()
    if tmp[1] == '(' or tmp[1] == ')':
        flag = 0
        if stack:
            if tmp[1] == '(' and stack[-1][1] == ')':
                result.append((stack.pop()[0], tmp[0]))
                flag = 1
        if not flag:
            stack.append(tmp)

answers = set()

for i in range(1, len(result)+1):
    for indexes in combinations(result, i):
        answer = input_str[::]
        for a, b in indexes:
            answer[a] = ''
            answer[b] = ''
        answers.add(''.join(answer))

for answer in sorted(answers):
    print(answer)
