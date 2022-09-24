def cal_date(date, term, term_list):
    y, m, d = date.split('.')
    y, m, d = int(y), int(m), int(d)
    m += int(term_list[term])
    d -= 1
    if m > 12:
        y += 1
        m -= 12
    if d == 0:
        d = 28
        m -= 1
    print(y, m, d)
    

def solution(today, terms, privacies):
    dates = []
    term_list = {}
    for term in terms:
        name, period = term.split()
        term_list[name] = period

    for i in range(len(privacies)):
        date, term = privacies[i].split()
        date = cal_date(date, term, term_list)
        dates.append(date)

        
        
    return dates