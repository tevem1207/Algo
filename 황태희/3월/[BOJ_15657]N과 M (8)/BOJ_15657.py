import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())
arr = sorted(map(int, input().split()))

answers = [[] for _ in range(M)]
answers[0] = [[num] for num in arr]

for i in range(1, M):
    for arr_a in answers[i-1]:
        for num in arr:
            if num >= arr_a[-1]:
                answers[i].append(arr_a+[num])

for answer in answers[-1]:
    print(*answer)