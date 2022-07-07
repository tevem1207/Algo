import sys
sys.stdin = open('input1.txt')


n = int(input())
arr = list(map(int, input().rsplit()))
answers = arr[:]

for i in range(n):
    max_tmp = 0
    for j in range(i):
        if arr[j] < arr[i]:
            max_tmp = max(max_tmp, answers[j])
    answers[i] += max_tmp

print(max(answers))
