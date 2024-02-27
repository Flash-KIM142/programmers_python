# 2022 KAKAO TECH INTERNSHIP
import heapq


def solution(alp, cop, problems):
    answer = 0
    INF = int(1e9)
    target_alp = 0
    target_cop = 0
    for problem in problems:
        target_alp = max(target_alp, problem[0])
        target_cop = max(target_cop, problem[1])
    if target_alp <= alp and target_cop <= cop:
        return 0

    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])
    dist = [[INF] * 151 for _ in range(151)]
    dist[alp][cop] = 0
    hq = []
    heapq.heappush(hq, (0, alp, cop))
    while hq:
        cur_time, cur_alp, cur_cop = heapq.heappop(hq)
        if cur_alp >= target_alp and cur_cop >= target_cop:
            answer = cur_time
            break
        if dist[cur_alp][cur_cop] < cur_time:
            continue

        for problem in problems:
            if cur_alp < problem[0] or cur_cop < problem[1]:
                continue
            nxt_time, nxt_alp, nxt_cop = cur_time + problem[4], cur_alp + problem[2], cur_cop + problem[3]
            if nxt_alp > target_alp:
                nxt_alp = target_alp
            if nxt_cop > target_cop:
                nxt_cop = target_cop
            if dist[nxt_alp][nxt_cop] > nxt_time:
                dist[nxt_alp][nxt_cop] = nxt_time
                heapq.heappush(hq, (nxt_time, nxt_alp, nxt_cop))

    return answer
