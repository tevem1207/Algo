import heapq


def solution(n, info):
    Q = []
    answer = [0 for _ in range(11)]
    stack = []
    cnt = n
    score = 0

    for i in range(10):
        if info[i]:
            score += (10 - i)

    for i in range(10):
        if info[i]:
            heapq.heappush(Q, (-(2 * (10 - i)) / (info[i] + 1), (info[i] + 1), i))
        else:
            heapq.heappush(Q, (-(10 - i), 1, i))

    while cnt > 0 and Q:
        target = heapq.heappop(Q)
        if target[1] <= cnt:
            answer[target[2]] = target[1]
            cnt -= target[1]
            score += int(target[0] * target[1])

    if score > 0:
        return [-1]
    else:
        if cnt > 0:
            answer[-1] += cnt
        return answer