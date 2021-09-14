# n=4
#
# history=[[0] * n for _ in range(26)]
#
# for i in range(26):
#     for j in range(4):
#         print(history[i])
#
# int(ord(pos[0]) - int(ord('a')))

length = 4
tmp=[]
n=2

for i in range(length):
    if length > i+n-1:
        for j in range(i,i+n):
            tmp.append(j)
        print(tmp)
        tmp=[]