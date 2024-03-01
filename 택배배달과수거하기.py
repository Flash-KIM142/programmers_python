def solution(cap, n, deliveries, pickups):
    # 배달과 수거 정보 스택에 각각 초기화
    del_left = []
    pck_left = []
    for i in range(n):
        if deliveries[i] > 0:
            del_left.append((i+1, deliveries[i]))
        if pickups[i] > 0:
            pck_left.append((i+1, pickups[i]))
    # cap만큼 각각 줄여나가기
    answer = 0
    while True:
        if not del_left and not pck_left:
            break
        far = 0
        del_cnt = cap
        while del_cnt != 0:
            if not del_left:
                break
            target_pos, target_num = del_left.pop()
            far = max(far, target_pos)
            tmp_flag = target_num - del_cnt
            if tmp_flag == 0:  # 딱 맞을 때
                break
            elif tmp_flag > 0:  # cap보다 더 많아서 다시 와야할 때
                del_left.append((target_pos, tmp_flag))
                break
            else:  # cap이 충분해서 다음 것까지 처리할 수 있을 때
                del_cnt -= target_num

        pck_cnt = cap
        while pck_left or pck_cnt != 0:
            if not pck_left:
                break
            target_pos, target_num = pck_left.pop()
            far = max(far, target_pos)
            tmp_flag = target_num - pck_cnt
            if tmp_flag == 0:
                break
            elif tmp_flag > 0:
                pck_left.append((target_pos, tmp_flag))
                break
            else:
                pck_cnt -= target_num
        answer += far

    return answer * 2


result = solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])
print(result)