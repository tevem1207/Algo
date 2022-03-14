import sys
'''
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 5
'''
sys.stdin = open('input.txt')

n = int(input())
d = [1, 2]

for i in range(2, n):
    d.append(d[i-1] + d[i-2])

print(d[n-1] % 10007)
