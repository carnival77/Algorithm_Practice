def solution(board, moves):
    answer = 0

    n = len(board)
    bucket = []

    for move in moves:
        for i in range(n):
            if board[i][move - 1] != 0:
                bucket.append(board[i][move - 1])
                board[i][move - 1] = 0

                if len(bucket) >= 2:
                    if bucket[-1] == bucket[-2]:
                        answer += 1
                        bucket.pop(-1)
                        bucket.pop(-1)
                break

    return answer * 2