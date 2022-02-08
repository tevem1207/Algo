def solution(a, b):
    answer = 0
    if a == b:
        answer = a
    
    elif a > b:
        for idx in range(b, a+1):
            answer += idx
    else:
        for idx in range(a, b+1):
            answer += idx
    return answer