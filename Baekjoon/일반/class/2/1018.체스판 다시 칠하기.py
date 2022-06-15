n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
b1=[list("WBWBWBWB"),list("BWBWBWBW")] *4
b2=[list("BWBWBWBW"),list("WBWBWBWB")] *4

ans=1e9

def go(b):
    dif=0

    for i in range(8):
        for j in range(8):
            if a[x + i][y + j] != b[i][j]:
                pass
            elif a[x + i][y + j] != b[i][j]:
                pass
            else:
                dif += 1

    return dif

for x in range(n):
    for y in range(m):
        lx, ly = x + 7, y + 7
        if lx < n and ly < m:
            ans=min(ans,go(b1),go(b2))
print(ans)