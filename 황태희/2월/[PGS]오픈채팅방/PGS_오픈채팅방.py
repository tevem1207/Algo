def solution(record):
    answer = []
    record_list = []
    uid = {}
    for message in record:
        user_info = message.split()
        if user_info[0] != 'Change':
            record_list.append(user_info[:2])
        if user_info[0] != 'Leave':
            uid[user_info[1]] = user_info[2]
    
    for i in record_list:
        if i[0] == 'Enter':
            answer.append(f'{uid[i[1]]}님이 들어왔습니다.')
        else:
            answer.append(f'{uid[i[1]]}님이 나갔습니다.')
    
    return answer