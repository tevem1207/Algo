import sys 
sys.stdin = open('input1.txt')


N, M = map(int, input().split())
print(*sorted(list(map(int, input().split())) + list(map(int, input().split()))))
