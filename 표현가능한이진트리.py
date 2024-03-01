def dec_to_bin(num):
    result = []
    while num > 0:
        result.append(num % 2)
        num //= 2
    cnt = 1
    while True:
        if len(result) < cnt:
            break
        cnt *= 2
    concat_zero_num = cnt - 1 - len(result)
    for _ in range(concat_zero_num):
        result.append(0)
    result.reverse()
    return result


def is_tree(nodes):
    if len(nodes) == 1:
        return True
    mid_idx = len(nodes) // 2
    left_tree = nodes[:mid_idx]
    right_tree = nodes[mid_idx + 1:]
    if nodes[mid_idx] == 0:
        if left_tree[len(left_tree) // 2] == 1 or right_tree[len(right_tree) // 2] == 1:
            return False

    return is_tree(left_tree) and is_tree(right_tree)


def solution(numbers):
    answer = []
    for number in numbers:
        tmp = dec_to_bin(number)
        if is_tree(tmp):
            answer.append(1)
        else:
            answer.append(0)
    return answer
