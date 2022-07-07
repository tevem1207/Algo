import sys 
sys.stdin = open('input1.txt')


N, K = map(int, input().split())
S = list(map(int, input().split()))
end = tmp = result = count = 0

for start in range(N):
    while count <= K and end < N:
        if S[end] % 2 == 1:
            count += 1
        else:
            tmp += 1
        end += 1

        if start == 0 and end == N:
            result = tmp
            break

    if count == K + 1:
        result = max(tmp, result)

    if S[start] % 2 == 1:
        count -= 1
    else:
        tmp -= 1

print(result)
