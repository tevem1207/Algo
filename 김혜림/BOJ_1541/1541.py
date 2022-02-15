# 잃어버린 괄호

import sys
sys.stdin = open('input.txt')

for _ in range(3):
    # 빼기 연산자를 기준으로 한다!!!
    result = 0
    formula = input().split('-')
    
    if len(formula) == 1:
        for num in formula[0].split('+'):
            result += int(num)
    
    else:            
        for nums in formula[1::]:
            num = nums.split('+')
            for n in num:
                result -= int(n)   
                
        for num in formula[0].split('+'):
            result += int(num)
    
    print(result)