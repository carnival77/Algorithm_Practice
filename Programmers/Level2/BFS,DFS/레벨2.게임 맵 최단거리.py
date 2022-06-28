from collections import deque


def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((0, 0))
    dist = [[-1] * m for _ in range(n)]
    dist[0][0] = 1

    while (q):
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and maps[nx][ny] == 1:
                dist[nx][ny] = dist[x][y] + 1
                if nx == n - 1 and ny == m - 1:
                    return dist[nx][ny]
                else:
                    q.append((nx, ny))

    return -1ㅇ