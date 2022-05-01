"""
단품으로만 제공하던 메뉴를 조합해서 코스요리 형태로 재구성해서 새로운 메뉴
코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성
최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 후보에 포함
가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성하기로 했습니다.
"""
from itertools import combinations


def solution(orders, course):
    answer = []
    
    # 0. 최대 메뉴 길이 찾기
    max_len = 0
    for order in orders:
        if len(order) > max_len:
            max_len = len(order)
    
    i = 0
    while i < len(course):
        if course[i] > max_len:
            course.pop(i)
        else:
            i += 1
    
    # 1. 조합 찾아서 딕셔너리에 넣기 
    for c in course:
        menus = {}
        for order in orders:
            order = sorted(list(order))
            ords_combi = list(combinations(order, c))
            for ord_combi in ords_combi:
                if not menus.get(ord_combi):
                    menus[ord_combi] = 1
                else:
                    menus[ord_combi] += 1
        
        # 2. 주문 개수 최대인 아이 찾기
        max_k = []
        max_v = 0
        for k, v in menus.items():
            if v > max_v:
                max_v = v
                max_k = [k]
            elif v == max_v:
                max_k.append(k)
        
        # 3. 정답 넣기
        if max_v >= 2:
            for k in max_k:
                answer.append(''.join(k))
            answer.sort()
    return answer


orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
# return 형태 ["WX","XY"]
print(solution(orders, course))
