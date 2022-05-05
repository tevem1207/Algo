import sys 
sys.stdin = open('input3.txt')


def zoac(str, result):
    min_alpha = (str[0], 0)
    for i in range(len(str)):
        if str[i][1] < min_alpha[0][1]:
            min_alpha = (str[i], i)
    result[min_alpha[0][0]] = min_alpha[0][1]
    print(''.join(result))
    # print(result)
    if min_alpha[1] != len(str) - 1:
        zoac(str[min_alpha[1]+1:], result)

    if str[:min_alpha[1]]:
        zoac(str[:min_alpha[1]], result)


string = list(enumerate(input().strip()))
zoac(string, ['' for _ in range(len(string))])
