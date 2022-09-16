import sys
input=sys.stdin.readline

n=int(input())
d=[int(1e9)] * (n+1)
# d[0]=d[1]=d[2]=d[4]=d[7]=-1
# d[3]=d[5]=1

for i in range(n+1):
    if i==3:
        d[i]=1
    elif i==5:
        d[i]=1
    else:
        if i>3 and -1<d[i - 3] < int(1e9):
            d[i]=min(d[i],d[i-3]+1)
        if i>5 and -1< d[i - 5] < int(1e9):
            d[i]=min(d[i],d[i-5]+1)
        if not (i>3 and -1<d[i - 3] < int(1e9)) and not (i>5 and -1< d[i - 5] < int(1e9)):
            d[i]=-1

# print(d)
print(d[n])