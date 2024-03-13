def solution(numbers, hand):
    answer = ''
    number_pos = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    left_hand = [3, 0]
    right_hand = [3, 2]
    for num in numbers:
        if num == 1 or num == 4 or num == 7:  # left_hand
            answer += 'L'
            left_hand = number_pos[num]
        elif num == 3 or num == 6 or num == 9:  # right_hand
            answer += 'R'
            right_hand = number_pos[num]
        else:
            cur_num_pos = number_pos[num]
            left_hand_dist = abs(cur_num_pos[0] - left_hand[0]) + abs(cur_num_pos[1] - left_hand[1])
            right_hand_dist = abs(cur_num_pos[0] - right_hand[0]) + abs(cur_num_pos[1] - right_hand[1])
            if left_hand_dist < right_hand_dist:  # left_hand
                answer += 'L'
                left_hand = cur_num_pos
            elif right_hand_dist < left_hand_dist:  # right_hand
                answer += 'R'
                right_hand = cur_num_pos
            else:  # which hand you use
                if hand == "left":
                    answer += 'L'
                    left_hand = cur_num_pos
                else:
                    answer += 'R'
                    right_hand = cur_num_pos
    return answer
