import sys
sys.stdin = open('input2.txt')


def whos_winner(A, B):
    a_score = [0]*5
    b_score = [0]*5
    
    for a in A[1:]:
        a_score[a] += 1
    for b in B[1:]:
        b_score[b] += 1
    
    for i in range(4, 0, -1):
        if a_score[i] == b_score[i]:
            continue
        elif a_score[i] > b_score[i]:
            return 'A'
        else:
            return 'B'
    return 'D'
    
    
N = int(input())

for _ in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    print(whos_winner(A, B))