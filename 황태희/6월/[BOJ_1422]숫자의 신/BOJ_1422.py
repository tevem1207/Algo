import sys 
sys.stdin = open('input1.txt')

K, N = map(int, input().split())
numbers = []
answer = ''

for _ in range(K):
    number = input().strip()
    r_number = number
    while len(number) < 10:
        number += number
    numbers.append((number, r_number))

numbers = sorted(numbers, reverse=True)
max_num = max(numbers, key=lambda x: int(x[1]))

flag = 1
for number in numbers:
    if flag and number == max_num:
        flag = 0
        for _ in range(N - K):
            answer += number[1]
    answer += number[1]

print(answer)
