def solution(board, skill):
    N, M = len(board[0]), len(board)
    matrix = [[0 for _ in range(N+1)] for _ in range(M+1)]
    answer = 0
    
    # skill 연산
    for s in skill:
        n = (s[0]*2-3) * s[5]
        x, y = s[4] - s[2], s[3] - s[1]
        if x or y:
            matrix[s[1]+y+1][s[2]+x+1] += n
            matrix[s[1]][s[2]+x+1] -= n
            matrix[s[1]+y+1][s[2]] -= n
            matrix[s[1]][s[2]] += n
    
    for i in range(M):
        for j in range(N):
            matrix[i][j+1] += matrix[i][j]

    for i in range(M):
        for j in range(N):
            matrix[i+1][j] += matrix[i][j]
            board[i][j] += matrix[i][j]
            if board[i][j] > 0:
                answer += 1
    
    return answer