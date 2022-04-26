def solution(n, info):
    answer = [[], 0]
    result = [0 for _ in range(11)]
    target = 0
    for i in range(11):
        if info[i]:
            target += 10 - i

    def dfs(score, cnt):
        flag = 1
        for i in range(11):
            arrow = info[i] + 1
            if cnt - arrow >= 0 and not result[i]:
                flag = 0
                result[i] = arrow

                if info[i]:
                    dfs(score + 2 * (10 - i), cnt - arrow)
                else:
                    dfs(score + (10 - i), cnt - arrow)

                result[i] = 0

        if flag:
            if score > answer[1]:
                answer[0] = result[::]
                answer[0][-1] += cnt
                answer[1] = score
            elif score == answer[1]:
                for i in range(11)[::-1]:
                    if result[i] > answer[0][i]:
                        answer[0] = result[::]
                        answer[0][-1] += cnt
                        break
                    elif answer[0][i] > result[i]:
                        break

    dfs(0, n)

    if answer[1] - target > 0:
        return answer[0]
    else:
        return [-1]