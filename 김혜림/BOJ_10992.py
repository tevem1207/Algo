# 규칙 유추해서 별 찍기
# 마지막 줄은 입력 n번째 홀수

space = ' '
star = '*'
n = int(input())

if n == 1:
    print('*')

else: 
    for i in range(n, 0, -1):
        if i == n:
            print(space*(n-1), star, sep='')

        elif i == 1:
            print(star * (2*n-1))
            
        else:
            print(space*(i-1), star, space*(2*(n-i)-1), star, sep='')    





