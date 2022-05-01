"""
강의 서쪽에는 N개의 사이트, 동쪽에는 M개의 사이트 (N ≤ M)
다리를 최대한 많이 지으려고 하기 때문에 서쪽의 사이트 개수만큼 (N개) 다리를 지으려고 한다. 
다리끼리는 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수를 구하는 프로그램을 작성하라.
"""
import sys
sys.stdin = open('input.txt')


from math import factorial

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    
    # 순서가 정해진 순열 => 조합!
    answer = factorial(M) / (factorial(N) * factorial(M-N))
    print(int(answer))