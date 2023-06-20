import sys
from collections import defaultdict

n = 3
m = 3
a = [[0] * 100 for _ in range(100)]

r, c, k = map(int,input().split())
r -= 1
c -= 1

for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(m):
        a[i][j] = temp[j]

if a[r][c] == k:
    print(0)
    sys.exit(0)

for t in range(1, 101):
    if n >= m:
        mm = m
        for i in range(n):
            d = defaultdict(int)
            for j in range(n):
                if a[i][j] == 0:
                    continue
                d[a[i][j]] += 1
            v = []
            for key, val in d.items():
                v.append((val,key))
            v.sort()
            l = min(len(v), 50)
            for j in range(l):
                a[i][j*2] = v[j][1]
                a[i][j*2+1] = v[j][0]
            for j in range(l*2, 100):
                a[i][j] = 0
            if mm < len(v)*2:
                mm = len(v)*2
        m = mm
    else:
        nn = n
        for j in range(m):
            d = defaultdict(int)
            for i in range(n):
                if a[i][j] == 0:
                    continue
                d[a[i][j]] += 1
            v = []
            for key, val in d.items():
                v.append((val,key))
            v.sort()
            l = min(len(v), 50)
            for i in range(l):
                a[i*2][j] = v[i][1]
                a[i*2+1][j] = v[i][0]
            for i in range(l*2, 100):
                a[i][j] = 0
            if nn < len(v)*2:
                nn = len(v)*2
        n = nn
    if a[r][c] == k:
        print(t)
        sys.exit(0)
print(-1)