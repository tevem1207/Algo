import sys 
sys.stdin = open('input1.txt') 

input_str = input()
tmp = input_str[0]
cnt = 1
cnt_tmp = 0

if tmp != 'w' or input_str[-1] != 'f':
    print(0)
else:
    for i in range(1, len(input_str)):
        if tmp == input_str[i]:
            cnt += 1
            if input_str[i] != 'w':
                if cnt_tmp < cnt:
                    print(0)
                    break
        elif tmp == 'w' and input_str[i] == 'o':
            cnt_tmp = cnt
            cnt = 1
        elif (tmp == 'o' and input_str[i] == 'l') or (tmp == 'l' and input_str[i] == 'f') or (tmp == 'f' and input_str[i] == 'w'):
            if cnt_tmp == cnt:
                cnt = 1
            else:
                print(0)
                break
        else:
            print(0)
            break
        tmp = input_str[i]
    else:
        if cnt_tmp == cnt:
            print(1)
        else:
            print(0)
