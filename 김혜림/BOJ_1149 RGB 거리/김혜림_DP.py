import sys
sys.stdin = open('input.txt')

choices = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}
N = int(input())

# 한 행의 상황에서 최솟값인 경우를 저장하는 리스트
tmp = [0, 0, 0]
for _ in range(N):
    arr = list(map(int, input().split()))
    for i in range(3):
        arr[i] += min(tmp[choices[i][0]], tmp[choices[i][1]])
    tmp = arr

print(min(tmp))