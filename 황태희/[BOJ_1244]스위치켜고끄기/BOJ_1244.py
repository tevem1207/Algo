import sys
sys.stdin = open('input.txt')


N = int(input())
switches = list(map(int, input().split()))
M = int(input())

for _ in range(M):
    student, i = map(int, input().split())

    if student == 1:
        for idx in range(i-1, N, i):
            if switches[idx]:
                switches[idx] = 0
            else:
                switches[idx] = 1

    else:
        new_switches = switches[:]
        stack = [switches.pop() for _ in range(N - i)]
        cnt = 0
        if switches.pop():
            new_switches[i-1] = 0
        else:
            new_switches[i-1] = 1

        if switches and stack:
            while stack[-1] == switches[-1]:
                stack.pop()
                switches.pop()
                cnt += 1
                if not stack or not switches:
                    break

        for idx in range(1, cnt+1):
            if new_switches[i-1-idx]:
                new_switches[i - 1 - idx] = 0
                new_switches[i - 1 + idx] = 0
            else:
                new_switches[i - 1 - idx] = 1
                new_switches[i - 1 + idx] = 1

        switches = new_switches

while len(switches) != 0:
    print(*switches[:20])
    switches = switches[20:]
