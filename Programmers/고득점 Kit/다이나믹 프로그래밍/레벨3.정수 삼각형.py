def solution(triangle):
    a = triangle
    n = len(a[-1])

    d = [[0] * n for _ in range(n)]

    a.reverse()

    for i in range(n):
        d[0][i] = a[0][i]

    for i in range(1, n):
        for j in range(n - i):
            d[i][j] = max(d[i][j], d[i - 1][j] + a[i][j], d[i - 1][j + 1] + a[i][j])

    answer = d[n - 1][0]

    return answer