N = list(input())

opers = []

for i in range(len(N)):
    if N[i] == '+' or N[i] == '-':
        opers.append(N[i])
        N[i] = ' '

N = ''.join(N)

N = list(map(int, N.split()))

answer = N[0]
minus = 0

for i in range(len(opers)):
    if minus:
        answer -= N[i+1]
    else:
        if opers[i] == '+':
            answer += N[i+1]
        else:
            minus = 1
            answer -= N[i+1]

print(answer)
