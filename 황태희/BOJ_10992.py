N = int(input())

for floor in range(N):

    if floor == N - 1:
        print('*' * (N * 2 - 1))
        
    else:
        for i in range(floor + N):
            if i == (N-1) - floor or i == (N-1) + floor:
                print ('*', end = '')
            else:
                print(' ', end = '')
    print('')