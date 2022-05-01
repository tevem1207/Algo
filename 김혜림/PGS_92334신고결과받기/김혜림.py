def solution(id_list, report, k):
    report = list(set(report))
    id_cnt = {}
    for id in id_list:
        id_cnt[id] = [set(), 0]  # [신고한 유저, 신고당한 횟수]
    
    for rep in report:
        a, b = rep.split()
        id_cnt[a][0].add(b) 
        id_cnt[b][1] += 1
    
    banned_user = set()
    for key, val in id_cnt.items():
        if val[1] >= k:
            banned_user.add(key)

    answer = [0] * (len(id_list))
    for key, val in id_cnt.items():
        sset = val[0] & banned_user
        answer[id_list.index(key)] += len(sset)
    
    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))