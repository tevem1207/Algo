N = int(input())
number = 2

while N > 1:
    while not N % number:
        print(number)
        N /= number
    number += 1