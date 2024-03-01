def date_to_days(date, due):
    year, month, day = map(int, date.split('.'))
    if due > 0:
        month += due
        day -= 1
    return year * 12 * 28 + month * 28 + day


def solution(today, terms, privacies):
    answer = []
    # 오늘 날짜 day 값으로 초기화
    today_days = date_to_days(today, 0)
    # 약관 종류 정보 초기화
    term_info = dict()
    for term in terms:
        type, due = term.split()
        term_info[type] = int(due)
    # 각각 정보마다 유효 기간 지났는지 판별
    idx = 1
    for privacy in privacies:
        cur_date, cur_type = privacy.split()
        cur_date_to_days = date_to_days(cur_date, term_info[cur_type])
        if cur_date_to_days < today_days:
            answer.append(idx)
        idx += 1
    return answer


result = solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
print(result)
