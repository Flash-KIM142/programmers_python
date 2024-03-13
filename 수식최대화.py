from itertools import permutations
import copy


def calculator(num1, num2, operator):
    if operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2
    else:
        return num1 * num2


def solution(expression):
    answer = 0
    expression_list = list(expression)
    operator_candidates = ['-', '+', '*']

    expression = expression.replace('-', ' - ')
    expression = expression.replace('+', ' + ')
    expression = expression.replace('*', ' * ')
    expression_list = expression.split(' ')

    operator_combs = list(permutations(operator_candidates, 3))
    for operator_comb in operator_combs:
        tmp_list = copy.deepcopy(expression_list)
        for operator in operator_comb:
            while operator in tmp_list:
                operator_idx = tmp_list.index(operator)
                insert_value = calculator(int(tmp_list[operator_idx - 1]), int(tmp_list[operator_idx + 1]), operator)
                del tmp_list[operator_idx + 1]
                del tmp_list[operator_idx]
                del tmp_list[operator_idx - 1]
                tmp_list.insert(operator_idx - 1, insert_value)
        answer = max(answer, abs(int(tmp_list[0])))
    return answer


print(solution("50*6-3*2"))
