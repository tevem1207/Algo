import numpy as np


def solution(board, skill):

    board = np.array(board)
    
    for sk in skill:
        if sk[0] == 2:
            board[sk[1]:sk[3]+1, sk[2]:sk[4]+1] += sk[5]
        else:
            board[sk[1]:sk[3]+1, sk[2]:sk[4]+1] -= sk[5]
    
    return np.size(np.where(board > 0)[0])