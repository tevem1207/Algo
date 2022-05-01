import sys, math
sys.stdin = open('input.txt')


def solution(n, k):
    answer = 0
    # 1. n을 k진수로 변환
    n_base = ''
    while n > 0:
        n_base += str(n%k)
        n //= k
    
    # 2. 소수 찾기
    numbers = n_base[::-1].split('0')    
    for num in numbers:
        if num and num != '1':
            num = int(num)
            is_prime = 1
            # 2-1. 소수찾기 시간 단축
            for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0:
                    is_prime = 0
                    break
            if is_prime:
                answer += 1
            
    return answer


n, k = map(int, input().split())
print(solution(n, k))