def solution(board, skill):
    row_len = len(board)
    col_len = len(board[0])
    cumulative_sum = [[0] * (col_len + 1) for _ in range(row_len + 1)]
    for s in skill:
        d = s[5]
        if s[0] == 1:
            d *= -1
        cumulative_sum[s[1]][s[2]] += d
        cumulative_sum[s[3]+1][s[4]+1] += d
        cumulative_sum[s[1]][s[4]+1] += -d
        cumulative_sum[s[3]+1][s[2]] += -d

    # row에 대해 누적합
    for i in range(row_len):
        for j in range(1, col_len):
            cumulative_sum[i][j] += cumulative_sum[i][j-1]

    # col에 대해 누적합
    for i in range(col_len):
        for j in range(1, row_len):
            cumulative_sum[j][i] += cumulative_sum[j-1][i]

    result = 0
    for i in range(row_len):
        for j in range(col_len):
            if board[i][j] + cumulative_sum[i][j] > 0:
                result += 1
    return result


answer = solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])
print(answer)
