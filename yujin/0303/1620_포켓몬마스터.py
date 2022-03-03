import sys
sys.stdin = open("input.txt")

N, M = map(int, sys.stdin.readline().split())

pocket_list = [sys.stdin.readline().strip() for _ in range(N)]

for t in range(M):
    ans = sys.stdin.readline().strip()
    if ans.isdecimal():
        print(pocket_list[int(ans) - 1])
    else:
        print(pocket_list.index(ans) + 1)