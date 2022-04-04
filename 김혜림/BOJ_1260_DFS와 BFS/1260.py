import sys
from collections import deque
sys.stdin = open('input2.txt')
input = sys.stdin.readline


def dfs(S):
    global visited
    to_visit = deque([S])
    result = []
    
    while to_visit:
        current = to_visit.pop()
        if not visited[current]:
            visited[current] = 1
            result.append(current)
            if numbers[current]:
                for num in numbers[current]:
                    if not visited[num]:
                        to_visit.append(num)
        
    return result    


def bfs(S):
    global visited
    to_visit = deque([S])
    result = []
    
    while to_visit:
        current = to_visit.popleft()
        if not visited[current]:
            visited[current] = 1
            result.append(current)
            if numbers[current]:
                for num in numbers[current]:
                    if not visited[num]:
                        to_visit.append(num)
        
    return result    


V, E, S = map(int, input().split())
numbers = [[] for _ in range(1001)]

for _ in range(E):
    s, e = map(int, input().split())
    numbers[s].append(e)
    numbers[e].append(s)

# 큰 수부터 정렬
for nums in numbers:
    if nums:
        nums.sort(reverse=True)
visited = [0] * (1001)
print(*dfs(S))

# 작은 수부터 정렬
for nums in numbers:
    if nums:
        nums.sort()
visited = [0] * (1001)
print(*bfs(S))
    