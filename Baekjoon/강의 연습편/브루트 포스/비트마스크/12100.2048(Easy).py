dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
LIMIT = 5


def gen(k):
    a = [0] * LIMIT
    for i in range(LIMIT):
        a[i] = (k & 3)
        k >>= 2
    return a


def check(a, dirs):
    n = len(a)
    d = [row[:] for row in a]

    for dir in dirs:
        ok = False
        merged = [[False] * n for _ in range(n)]

        while True:
            ok = False
            if dir == 0:
                for i in range(n - 2, -1, -1):
                    for j in range(n):
                        if d[i][j] == 0:
                            continue
                        if d[i + 1][j] == 0:
                            d[i + 1][j] = d[i][j]
                            merged[i + 1][j] = merged[i][j]
                            d[i][j] = 0
                            ok = True
                        elif d[i + 1][j] == d[i][j]:
                            if not merged[i][j] and not merged[i + 1][j]:
                                d[i + 1][j] *= 2
                                merged[i + 1][j] = True
                                d[i][j] = 0
                                ok = True
            elif dir == 1:
                for i in range(1, n):
                    for j in range(n):
                        if d[i][j] == 0:
                            continue
                        if d[i - 1][j] == 0:
                            d[i - 1][j] = d[i][j]
                            merged[i - 1][j] = merged[i][j]
                            d[i][j] = 0
                            ok = True
                        elif d[i - 1][j] == d[i][j]:
                            if not merged[i][j] and not merged[i - 1][j]:
                                d[i - 1][j] *= 2
                                merged[i - 1][j] = True
                                d[i][j] = 0
                                ok = True
            elif dir == 2:
                for j in range(1, n):
                    for i in range(n):
                        if d[i][j] == 0:
                            continue
                        if d[i][j - 1] == 0:
                            d[i][j - 1] = d[i][j]
                            merged[i][j - 1] = merged[i][j]
                            d[i][j] = 0
                            ok = True
                        elif d[i][j - 1] == d[i][j]:
                            if not merged[i][j] and not merged[i][j - 1]:
                                d[i][j - 1] *= 2
                                merged[i][j - 1] = True
                                d[i][j] = 0
                                ok = True
            elif dir == 3:
                for j in range(n - 2, -1, -1):
                    for i in range(n):
                        if d[i][j] == 0:
                            continue
                        if d[i][j + 1] == 0:
                            d[i][j + 1] = d[i][j]
                            merged[i][j + 1] = merged[i][j]
                            d[i][j] = 0
                            ok = True
                        elif d[i][j + 1] == d[i][j]:
                            if not merged[i][j] and not merged[i][j + 1]:
                                d[i][j + 1] *= 2
                                merged[i][j + 1] = True
                                d[i][j] = 0
                                ok = True
            if not ok:
                break

    ans = max([max(row) for row in d])
    return ans


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for k in range(1 << (LIMIT * 2)):
    dirs = gen(k)
    cur = check(a, dirs)
    if ans < cur:
        ans = cur
print(ans)