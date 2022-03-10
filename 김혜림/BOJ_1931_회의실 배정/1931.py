import sys
sys.stdin = open('input.txt')

N = int(input())

meetings = []
for _ in range(N):
    s, e = map(int, input().split())
    meetings.append((s, e))

max_meeting = 1
for i in range(N):
    n_meeting = 1
    A = set(range(meetings[i][0], meetings[i][1]+1))
    for j in range(i+1, N):
        B = set(range(meetings[j][0], meetings[j][1]+1))
        if 0 <= len(A & B) <= 1:
            n_meeting += 1
            A |= B
    if n_meeting > max_meeting:
        max_meeting = n_meeting

print(max_meeting)