import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
sorted_numbers = sorted(set(numbers))

n_dict = {}
for i, v in enumerate(sorted_numbers):
    n_dict[v] = i

ans = []
for num in numbers:
    ans.append(n_dict[num])

print(*ans)
