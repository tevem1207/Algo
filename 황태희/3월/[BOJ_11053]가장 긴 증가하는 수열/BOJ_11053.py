import sys
sys.stdin = open('input.txt')


def binary_search(array, target, left, right):
    middle_idx = (left+right)//2
    if array[middle_idx-1] < target <= array[middle_idx]:
        return middle_idx
    elif array[middle_idx] > target:
        return binary_search(array, target,left,middle_idx-1)
    elif array[middle_idx] < target:
        return binary_search(array, target,middle_idx+1,right)


N = int(input())
arr = [0] + list(map(int, input().split()))

dp1 = [0 for _ in range(N+1)]
dp2 = [0]

for i in range(1, N+1):
    if arr[i] > dp2[-1]:
        dp1[i] = len(dp2)
        dp2.append(arr[i])
    else:
        index = binary_search(dp2, arr[i], 1, len(dp2)-1)
        dp1[i] = index
        dp2[index] = arr[i]

print(max(dp1))
