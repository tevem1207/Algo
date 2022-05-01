import sys
sys.stdin = open('input.txt')

N = int(input())
numbers = list(map(int, input().split()))

acid = []
base = []
for n in numbers:
    # 산성 / 염기성
    acid.append(n) if n > 0 else base.append(n)

# 하나의 용액으로만 구성된 경우
if not(acid or base):
    if acid:
        acid.sort()
        print(acid[0], acid[1])
    else:
        base.sort()
        print(base[0], base[1])

else:
    acid.sort()
    base.sort()
    


        
    