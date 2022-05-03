import sys 
sys.stdin = open('input4.txt')

n = int(input())
dp = [0 for _ in range(50001)]
dp[1] = 1

for i in range(2, n + 1):
    min_value = float('inf')
    for j in range(1, int(i**(1/2))+1):
        tmp = dp[i-j**2] + 1
        if tmp < min_value:
            min_value = tmp
    dp[i] = min_value

print(dp[n])
