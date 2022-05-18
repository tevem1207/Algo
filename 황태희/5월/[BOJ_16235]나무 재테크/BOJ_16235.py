import sys 
sys.stdin = open('input1.txt')


from collections import deque


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

land = [[5 for _ in range(N)] for _ in range(N)]
trees = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

for _ in range(K):
    for i in range(N):
        for j in range(N):
            cnt = 0
            # 봄
            for k in range(len(trees[i][j])):
                if land[i][j] >= trees[i][j][k]:
                    land[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                else:
                    cnt += 1
            # 여름
            for _ in range(cnt):
                land[i][j] += trees[i][j].pop() // 2

    for i in range(N):
        for j in range(N):
            # 가을
            for k in range(len(trees[i][j])):
                if not trees[i][j][k] % 5:
                    for dj in [-1, 0, 1]:
                        for di in [-1, 0, 1]:
                            if dj == 0 and di == 0:
                                pass
                            elif 0 <= i + di < N and 0 <= j - dj < N:
                                trees[i + di][j - dj].appendleft(1)
            # 겨울
            land[i][j] += A[i][j]

total = 0
for i in range(N):
    for j in range(N):
        total += len(trees[i][j])

print(total)
