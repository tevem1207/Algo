def get_num(n, q):
    result = ''
    while n > 0:
        n, mod = divmod(n, q)
        result = str(mod) + result
    return result


def is_prime(num):
    if num < 4:
        return 1
    else:
        for n in range(2, int(num**(1/2))+1):
            if not num % n:
                return 0
    return 1
    

def solution(n, k):
    cnt = 0
    number = get_num(n, k)
    arr = number.split('0')
    
    for num in arr:
        if num and num != '1':
            num = int(num)
            cnt += is_prime(num)
    
    return cnt