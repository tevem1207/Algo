"""
상근이가 먼저 시작
1개 또는 3개를 가져가서
마지막 돌을 가져가면 승
"""

N = int(input())
winner = ''

if N%3 == 0: 
    winner = 'CY' if (N//3) % 2 == 0 else 'SK'
else:
    turn = N//3
    if N%3 == 1:
        turn += 1
    elif N%3 == 2:
        turn += 2
    
    winner = 'CY' if turn % 2 == 0 else 'SK'
print(winner)