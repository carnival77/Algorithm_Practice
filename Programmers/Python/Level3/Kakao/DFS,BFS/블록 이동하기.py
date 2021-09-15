# BFS. 맵 내 모든 부분으로 가는 경우의 수를 보드에 넣고, return board[n-1][m-1] 하면 최소경로.
# turn을 어떻게 해야 할 지만 고려해서 코딩하자. 최단거리와 경우의 수는 bfs 에서 q에 해당 경우를 append 안 하면 되고
# append된 경우는 알아서 되니 괜찮다.

from collections import deque

def get_next_pos(pos,board,n):

    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    next_pos = []

    p1,p2 = pos
    p1x, p1y = p1
    p2x, p2y = p2

    # 이동
    for direction in range(4):
        np1x = p1x + dx[direction]
        np1y = p1y + dy[direction]
        np2x = p2x + dx[direction]
        np2y = p2y + dy[direction]

        if np1x < 1 or np1x > n or np1y < 1 or np1y > n or  np2x < 1 \
                or np2x > n or np2y < 1 or np2y > n:
            continue
        if board[np1x][np1y] == 1 or board[np2x][np2y] == 1:
            continue
        if board[np1x][np1y] == 0 and board[np2x][np2y] == 0:
            next_pos.append({(np1x,np1y),(np2x,np2y)})

    # 턴
    # 현재 가로. 세로로 턴
    if p1x == p2x:
        # 위로 턴
        if board[p1x-1][p1y] == 0 and board[p2x-1][p2y] == 0:
            next_pos.append({(p1x,p1y),(p1x-1,p1y)})
            next_pos.append({(p2x,p2y),(p2x-1,p2y)})
        # 아래로 턴
        if board[p1x+1][p1y] == 0 and board[p2x+1][p2y] == 0:
            next_pos.append({(p1x,p1y),(p1x+1,p1y)})
            next_pos.append({(p2x,p2y),(p2x+1,p2y)})

    # 현재 세로. 가로로 턴
    elif p1y == p2y:
        # 왼쪽으로 턴
        if board[p1x][p1y-1] == 0 and board[p2x][p2y-1] == 0:
            next_pos.append({(p1x,p1y),(p1x,p1y-1)})
            next_pos.append({(p2x,p2y),(p2x,p2y-1)})
        # 오른쪽으로 턴
        if board[p1x][p1y+1] == 0 and board[p2x][p2y+1] == 0:
            next_pos.append({(p1x,p1y),(p1x,p1y+1)})
            next_pos.append({(p2x,p2y),(p2x,p2y+1)})

    return next_pos

def solution(board):
    n = len(board)

    new_board = [[1] * (n+2) for _ in range(n+2)]

    for x in range(n):
        for y in range(n):
            new_board[x+1][y+1] = board[x][y]

    visited = []

    start = {(1,1),(1,2)}
    q = deque()
    q.append((start,0))
    visited.append(start)

    while q:
        pos,count = q.popleft()

        print(pos,count)

        if (n,n) in pos:
            return count

        for next_pos in get_next_pos(pos,new_board,n):
            if next_pos not in visited:
                q.append((next_pos,count+1))
                visited.append(next_pos)

print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))