N, M = map(int, input().split())

numbers = list(map(int, input().split()))
length = len(numbers)


total = 0
min_diff = -300000

for first in range(length):
    for two in range(first+1, length):
        for third in range(two+1, length):
            total = numbers[first] + numbers[two] + numbers[third]
            diff = total - M
            if diff > 0:
                continue
            else:
                if diff > min_diff:
                    min_diff = diff

                        
print(M + min_diff)