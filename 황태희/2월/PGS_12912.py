def solution(a, b):
    
    tmp = abs(b - a)
    
    print(tmp)
    if not tmp % 2:
        return (b + a) * (tmp + 1) / 2
    
    return (b + a) * (tmp // 2 + 1)