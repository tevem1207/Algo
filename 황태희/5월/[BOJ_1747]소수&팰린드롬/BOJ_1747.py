import sys 
sys.stdin = open('input1.txt') 


def is_palindrome(string):
    for i in range(len(string)//2):
        if string[i] != string[-1-i]:
            return False
    else:
        return True


N = int(input())

if N < 3:
    print(2)
else:
    numbers = [1 for _ in range(1003002)]

    for i in range(2, 1003002):
        if numbers[i]:
            for j in range(2, 1003002):
                if i*j > 1003001:
                    break
                numbers[i*j] = 0

    while N < 1003002:
        if numbers[N]:
            if is_palindrome(str(N)):
                print(N)
                break
        N += 1
