import sys 
sys.stdin = open('input1.txt') 

html = input()
tmp = ''
i = 0

while i < len(html):
    if html[i] == '<':
        while html[i] != '>':
            if html[i] == '"':
                i += 1
                tmp = 'title : '
                while html[i] != '"':
                    tmp += html[i]
                    i += 1
                print(tmp)
                tmp = ''
            i += 1
    if html[i] != '>':
        tmp += html[i]
    elif html[i-3:i+1] == '</p>':
        tmp = tmp.strip().split()
        print(' '. join(tmp))
        tmp = ''
    i += 1
