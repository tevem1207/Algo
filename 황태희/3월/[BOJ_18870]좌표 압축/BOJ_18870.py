import sys
sys.stdin = open('input.txt')


def binary_search(target):
    left = 0
    right = length - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_numbers[mid] == target:
            return mid
        elif sorted_numbers[mid] > target:
            right = mid - 1
        else:
            left = mid + 1


N = int(input())

numbers = list(map(int, input().split()))

sorted_numbers = sorted(list(set(numbers)))
length = len(sorted_numbers)

for num in numbers:
    print(binary_search(num), end=' ')
