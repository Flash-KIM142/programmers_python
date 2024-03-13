from itertools import product


def solution(users, emoticons):
    answer = [0, 0]
    emoticons_len = len(emoticons)
    # 가능한 모든 할인 경우의 수 초기화
    tmp = []
    for i in range(1, 5):
        sales_percentage = i * 10
        tmp.append(sales_percentage)
    possible_sales = product(tmp, repeat=emoticons_len)
    # 각 할인의 경우마다 판단
    for sale in possible_sales:
        head_cnt = 0
        total_sales = 0
        for user in users:
            user_percentage, user_buy_limit = user[0], user[1]
            buy_sum = 0
            for i in range(emoticons_len):
                if sale[i] >= user_percentage:
                    buy_sum += emoticons[i] * (100 - sale[i]) / 100
            if buy_sum >= user_buy_limit:
                head_cnt += 1
            else:
                total_sales += buy_sum
        if answer[0] < head_cnt:
            answer[0] = head_cnt
            answer[1] = total_sales
        elif answer[0] == head_cnt and answer[1] < total_sales:
            answer[1] = total_sales
    return answer
