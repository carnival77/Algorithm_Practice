from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(p):
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                q = deque()
                q.append((i, j))
                dist = [[-1] * 5 for _ in range(5)]
                dist[i][j] = 0
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < 5 and 0 <= ny < 5 and dist[nx][ny] == -1 and p[nx][ny] != 'X':
                            dist[nx][ny] = dist[x][y] + 1
                            q.append((nx, ny))
                            if p[nx][ny] == 'P':
                                # md = abs(i - nx) + abs(j - ny)
                                # if md <= 2:
                                if dist[nx][ny]<=2:
                                    return 0
    return 1

def solution(places):
    ans=[1]*5

    for i,p in enumerate(places):
        ans[i]=bfs(p)

    return ans

places=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))