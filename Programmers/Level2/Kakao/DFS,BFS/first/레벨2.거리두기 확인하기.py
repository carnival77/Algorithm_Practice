from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, place):
    q = deque()
    visited = [[False] * 5 for _ in range(5)]
    q.append((x, y, 0))
    visited[x][y] = True

    while q:
        x, y, dist = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == False:
                if place[nx][ny] == "O" and dist < 1:
                    q.append((nx, ny, dist + 1))
                    visited[nx][ny] = True
                else:
                    if place[nx][ny] == "P":
                        return False
    return True


def solution(places):
    answer = [0] * len(places)

    for inx, place in enumerate(places):
        safe = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    if not bfs(i, j, place):
                        safe = False
                        break
            if safe == False:
                break

        if safe == False:
            answer[inx] = 0
        else:
            answer[inx] = 1

    return answer