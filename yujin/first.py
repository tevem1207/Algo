def solution(a, b):
    answer = 0
    
    if a>=b:
        while a>=b:
            answer +=b
            b+=1
    else:
        while b>=a:
            answer+=a
            a+=1
    return answer