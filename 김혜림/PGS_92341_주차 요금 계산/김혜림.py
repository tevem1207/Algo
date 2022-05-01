def solution(fees, records):
    basetime, basefee, pertime, perfee = fees[0], fees[1], fees[2], fees[3]

    # 1. 출입기록 나누기
    i_infos = {}
    o_infos = {}
    for record in records:
        t, n, io = record.split()
        # 1-1. 시간 계산하기
        t_minute = int(t[:2]) * 60 + int(t[3:])

        if io == 'IN':
            i_infos[n] = t_minute
        elif io == 'OUT':
            o_infos[n] = t_minute

    # 2. 시간계산 하기
    tmp_ans = []
    for k, v in i_infos.items():
        # 2-1. 주차시간 계산하고
        if o_infos.get(k):
            ptime = o_infos.get(k) - v
        else:   # 23:59 = 23*60 + 59 = 1440-1
            ptime = 1439 - v
        
        # 2-2. 요금 정산하기
        if ptime <= basetime:
            tmp_ans.append((k, basefee))
        else:
            fee = int((ptime-basetime) / pertime) * perfee + basefee
            tmp_ans.append((k, fee))
    tmp_ans.sort()
    
    # 3. 출력하기
    answer = []
    for tmp in tmp_ans:
        answer.append(tmp[1])
    
    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))