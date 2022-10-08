t=int(input())
mod=1000000009
MAX = 100000
d = [[0] * 4 for _ in range(MAX+1)]
d[1][1] = 1
d[2][2] = 1
d[3][2] = 1
d[3][1] = 1
d[3][3] = 1
for i in range(4, MAX+1):
    for j in range(1, 4):
        if j == 1:
            d[i][j] = d[i - 1][2] + d[i - 1][3]
        elif j == 2:
            d[i][j] = d[i - 2][1] + d[i - 2][3]
        else:
            d[i][j] = d[i - 3][1] + d[i - 3][2]
    d[i][1] %= 1000000009
    d[i][2] %= 1000000009
    d[i][3] %= 1000000009
for _ in range(t):
    n=int(input())
    print(sum(d[n])%1000000009)

# t=int(input())
#
# MAX = 100000
#
# mod = 1000000009
#
# d=[[0] * 4 for _ in range(MAX+1)]
#
# for i in range(1,MAX+1):
#     if i>=1:
#         d[i][1] = d[i-1][2] + d[i-1][3]
#         if i==1:
#             d[i][1]=1
#     if i>=2:
#         d[i][2] = d[i-2][1] + d[i-2][3]
#         if i==2:
#             d[i][2]=1
#     if i>=3:
#         d[i][3] = d[i-3][1] + d[i-3][2]
#         if i==3:
#             d[i][3]=1
#     d[i][1] %= mod
#     d[i][2] %= mod
#     d[i][3] %= mod
#
# for _ in range(t):
#     n=int(input())
#     print(sum(d[n])%mod)