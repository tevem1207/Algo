num = 1
N = 0
answers = [i for i in range(10001)]
while num < 10000:
    N = 0
    for n in str(num):
        N += int(n)
    N += num
    if N <= 10000:
        answers[N] = 0
    num += 1

for i in answers:
    if i:
        print(i)