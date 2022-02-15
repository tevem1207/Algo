
# 직관적 생각나는대로 막 풀기..잇츠 막노동
first = input()
second = input()
third = input()

if first == 'black':
    first = 0
elif first == 'brown':
    first = 1
elif first == 'red':
    first = 2
elif first == 'orange':
    first = 3
elif first == 'yellow':
    first = 4
elif first == 'green':
    first = 5
elif first == 'blue':
    first = 6
elif first == 'violet':
    first = 7
elif first == 'grey':
    first = 8
elif first == 'white':
    first = 9

if second == 'black':
    second = 0
elif second == 'brown':
    second = 1
elif second == 'red':
    second = 2
elif second == 'orange':
    second = 3
elif second == 'yellow':
    second = 4
elif second == 'green':
    second = 5
elif second == 'blue':
    second = 6
elif second == 'violet':
    second = 7
elif second == 'grey':
    second = 8
elif second == 'white':
    second = 9


if third == 'black':
    third = 1
elif third == 'brown':
    third = 10
elif third == 'red':
    third = 100
elif third == 'orange':
    third = 1000
elif third == 'yellow':
    third = 10000
elif third == 'green':
    third = 100000
elif third == 'blue':
    third = 1000000
elif third == 'violet':
    third = 10000000
elif third == 'grey':
    third = 100000000
elif third == 'white':
    third = 1000000000

print((10*first+second)*third)

#세개의 리스트를 만들 수 있을 것 같아요? 그래서 돌리면 더 빠를것 같긴하네요 ㅠ