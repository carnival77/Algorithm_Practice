h,w,x,y = map(int,input().split())

b=[]
for _ in range(h+x):
    b.append(list(map(int,input().split())))

a=[[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        b[i+x][j+y] -= b[i][j]

for i in range(h):
    for j in range(w):
        a[i][j] = b[i][j]

for i in range(h):
    print(" ".join(map(str,a[i])))