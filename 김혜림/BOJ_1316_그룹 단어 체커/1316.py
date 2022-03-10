import sys
sys.stdin = open('input.txt')


def is_group_word(word):
    cnts = []
    for char in word:
        if char not in cnts:
            cnts.append(char)
        elif char in cnts:
            if cnts[-1] == char:
                continue
            return False
    return True
    
    
T = int(input())

for _ in range(T):
    N = int(input())
    words = list(input() for _ in range(N))
    results = list(map(is_group_word, words))
    
    total = 0
    for result in results:
        total += int(result)
        
    print(total)