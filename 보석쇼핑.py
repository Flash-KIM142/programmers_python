import heapq
from collections import defaultdict


def solution(gems):
    l, r = 0, 0
    type_num = len(set(gems))
    hq = []
    tmp_dict = defaultdict(int)
    while True:
        if r == len(gems) and len(tmp_dict) < type_num:
            break

        if len(tmp_dict) < type_num:  # r 1 증가
            tmp_dict[gems[r]] += 1
            r += 1
        else:  # 현재 [l, r] 우선순위큐에 삽입 후 l 1 증가
            heapq.heappush(hq, (r - l, [l + 1, r]))
            tmp_dict[gems[l]] -= 1
            if tmp_dict[gems[l]] == 0:
                del (tmp_dict[gems[l]])
            l += 1
    return hq[0][1]


res = solution([1, 2, 2, 2, 3, 1])
print(res)
