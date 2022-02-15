num = int(input())
final= 2*num-1

for i in range(1, num+1):
    if i==1:
        print(' '*(num-i),'*',sep='')
    elif i == num:
        print('*'*final)
    else:
        print(' '*(num-i),'*',' '*(2*i-3),'*',sep='')

    
