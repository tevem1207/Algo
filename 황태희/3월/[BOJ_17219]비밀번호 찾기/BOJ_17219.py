import sys
sys.stdin = open('input.txt')

import sys


input = sys.stdin.readline

N, M = map(int, input().split())

my_dict = {}

for _ in range(N):
    address, password = input().split()
    my_dict[address] = password

for _ in range(M):
    address = input().rstrip()
    print(my_dict[address])
