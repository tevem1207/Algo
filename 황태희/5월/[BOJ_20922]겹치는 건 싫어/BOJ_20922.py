import sys 
sys.stdin = open('input1.txt')


N, K = map(int, input().split())
arr = list(map(int, input().split()))
visited = {num: 0 for num in arr}
start = end = 0
answer = 1
visited[arr[0]] += 1

while end < N-1:
    end += 1
    visited[arr[end]] += 1
    if visited[arr[end]] > K:
        while visited[arr[end]] > K:
            visited[arr[start]] -= 1
            start += 1

    if answer < end-start+1:
        answer = end-start+1

print(answer)
