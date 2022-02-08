# 수 정렬하기

n_length = int(input())


numbers = []
for i in range(n_length):
    number = int(input())
    numbers.append(number)



numbers.sort()

for number in numbers:
    print(number)