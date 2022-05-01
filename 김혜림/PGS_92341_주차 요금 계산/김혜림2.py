import math
def solution(fees, records):
    basetime, basefee, pertime, perfee = fees[0], fees[1], fees[2], fees[3]
    tmp_ptime = {}

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
            
            # 2. 시간계산하기 
            ptime = o_infos[n] - i_infos[n]
            if not tmp_ptime.get(n):
                tmp_ptime[n] = ptime
            else:
                tmp_ptime[n] += ptime

            # 2-2. 시간계산 후 출입기록 지우기
            del i_infos[n], o_infos[n]
            
    # 출차기록이 없어서 남아있는 경우    
    if i_infos:
        for k, v in i_infos.items():
            ptime = 1439 - v
            
            if not tmp_ptime.get(k):
                tmp_ptime[k] = ptime
            else:
                tmp_ptime[k] += ptime
    
    # 3. 요금계산하기
    tmp_ans = []
    for num, parktime in tmp_ptime.items():
        if parktime <= basetime:
            tmp_ans.append([num, basefee])
        else:
            fee = math.ceil((parktime - basetime) / pertime) * perfee + basefee
            tmp_ans.append([num, fee])

    answer = []
    for ans in sorted(tmp_ans):
        answer.append(ans[1])

    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
           "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))