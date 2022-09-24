def cal_date(date, term, term_list):
    y, m, d = date.split('.')
    y, m, d = int(y), int(m), int(d)
    m += int(term_list[term])
    if m > 12:
        y += 1
        m -= 12
    return y, m, d

def is_valid(y,m,d, t_y, t_m, t_d):
    # 1. 년도로 구분
    if t_y > y: # 1-1. 연도가 지났을 때
        return True # 만료 됐다
    else: # 1-2. 년도가 올해거나 아직 남았을 때

        # 2. 달로 구분
        if t_m <= m: # 2-1. 오늘자 달과 같은 월이거나 아직 남았을 때
            if t_m < m: # 이번 달 이후에 만료면
                return False # 아직 만료 안 됨
            
            # 3. 달이 이번달이어서 년, 월까지 똑같고 이제 일자만 비교
            else:
                if t_d >= d: # 3-1. 일자가 같거나 지났으면
                    return True # 만료
                else: # 3-2. 일자가 남았으면
                    return False # 만료 안 됨
        else: # 2-2. 달이 지났다면
            return True

def solution(today, terms, privacies):
    answer = []
    term_list = {}
    t_y, t_m, t_d = today.split('.')
    t_y, t_m, t_d = int(t_y), int(t_m), int(t_d)
    for term in terms:
        name, period = term.split()
        term_list[name] = period

    for i in range(len(privacies)):
        date, term = privacies[i].split()
        y, m, d = cal_date(date, term, term_list)
        if is_valid(y,m,d, t_y, t_m, t_d):
            answer.append(i+1) # 유효기간이 True로 지난 애들 출력

    return answer


# def cal_date(date, term, term_list):
#     y, m, d = date.split('.')
#     y, m, d = int(y), int(m), int(d)
#     m += int(term_list[term])
#     d -= 1
#     if m > 12:
#         y += 1
#         m -= 12
#     if d == 0:
#         d = 28
#         m -= 1
#     return y, m, d

# def is_valid(y,m,d, t_y, t_m, t_d):
#     print(y, m, d)
#     if t_y <= y and t_m <= m and t_d <= d:
#         return True 
#     else:
#         return False # 만료 전

# def solution(today, terms, privacies):
#     answer = []
#     term_list = {}
#     t_y, t_m, t_d = today.split('.')
#     t_y, t_m, t_d = int(t_y), int(t_m), int(t_d)
#     for term in terms:
#         name, period = term.split()
#         term_list[name] = period

#     for i in range(len(privacies)):
#         date, term = privacies[i].split()
#         y, m, d = cal_date(date, term, term_list)
#         if not is_valid(y,m,d, t_y, t_m, t_d):
#             answer.append(i+1)

#     return answer