import sys
sys.stdin = open('input1.txt')


from bisect import bisect_left


n = int(input())
arr = list(map(int, input().rsplit()))
dp = [0 for _ in range(n)]
lis = []

for i in range(n):
    if not lis:
        lis.append(arr[i])
        dp[i] = len(lis)
    if lis[-1] < arr[i]:
        lis.append(arr[i])
        dp[i] = len(lis)
    else:
        index = bisect_left(lis, arr[i])
        lis[index] = arr[i]
        dp[i] = index + 1

ans = max(dp)
print(ans)

target = ans
answer = []

for i in range(n)[::-1]:
    if dp[i] == target:
        answer.append(arr[i])
        target -= 1

print(*answer[::-1])
