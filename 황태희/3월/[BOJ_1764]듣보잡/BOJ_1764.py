import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())

names_dict = {}
answer = []

for _ in range(N):
    name = input().rstrip('\n')
    names_dict[name] = 0

for _ in range(M):
    name = input().rstrip('\n')
    if name in names_dict:
        answer.append(name)

len_answer = len(answer)
print(len_answer)
for name in sorted(answer):
    print(name)
