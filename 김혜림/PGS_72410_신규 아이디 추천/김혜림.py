"""
아이디의 길이는 3자 이상 15자 이하여야 합니다.
아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.

1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
"""


def solution(new_id):
    answer = ''
    # 1. 대문자 -> 소문자
    new_id = new_id.lower()
    
    # 2. 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)만 남기기
    i = 0
    while i <= len(new_id)-1:
        ascii_n = ord(new_id[i])
        if 97 <= ascii_n <= 122 or 48 <= ascii_n <= 57 or ascii_n == 95 or ascii_n == 45 or ascii_n == 46:
            i += 1
        else:
            new_id = new_id[:i] + new_id[i+1:]
    
    # 3. 마침표 압축 4. 마침표가 맨앞 맨뒤인 경우 없애기
    idx = tmp = 0
    while idx <= len(new_id)-1:
        if new_id[idx] == '.':
            if idx == 0:
                new_id = new_id[1:]
            elif idx == len(new_id)-1:
                new_id = new_id[:-1]
                idx += 1
            elif new_id[idx+1] == '.':
                new_id = new_id[:idx] + new_id[idx+1:]
            else:
                idx += 1
        else:
            idx += 1
    
    # 5. 빈문자열 -> a로 채우기, 6. 16자 이상이면 15자 제한하고, 마침표있으면 제거, 7.2자 이하라면 맨 마지막 반복해서 3자로 만들기
    if not new_id:
        new_id = 'aaa'
        answer = new_id
    else:
        if len(new_id) > 15:
            answer = new_id[:15]
            if answer[-1] == '.':
                answer = answer[:-1]
        elif len(new_id) < 3:
            answer = new_id + new_id[-1]*(3-len(new_id))
        else:
            answer = new_id
                
    return answer


new_id = "abcdefghijklmn.p"

print(solution(new_id))