def solution(info, query):
    N = len(info)
    ALL = set(range(len(info)))
    answer = [0 for _ in range(len(query))]
    language = {'cpp': set(), 'java': set(), 'python': set(), '-': ALL}
    job = {'backend': set(), 'frontend': set(), '-': ALL}
    career = {'junior': set(), 'senior': set(), '-': ALL}
    food = {'chicken': set(), 'pizza': set(), '-': ALL}
    
    for i in range(N):
        info[i] = info[i].split()
        language[info[i][0]].add(i)
        job[info[i][1]].add(i)
        career[info[i][2]].add(i)
        food[info[i][3]].add(i)

    for i in range(len(query)):
        case = query[i].replace('and ', '').split()
        tmp = language[case[0]] & job[case[1]] & career[case[2]] & food[case[3]]
        for j in tmp:
            if int(info[j][4]) >= int(case[4]):
                answer[i] += 1
        
    return answer