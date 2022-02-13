N = int(input())
limit = 1000
numbers = [None] * (limit * 2 + 1)

for _ in range(N):
    number = int(input())
    numbers[number + limit] = number

for number in numbers:
    if not number is None:
        print(number)