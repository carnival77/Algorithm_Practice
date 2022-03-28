n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())

answer=0

for i in range(n):
    answer+=1
    if a[i]<=b:
        a[i]=0
    else:
        a[i]-=b

    share = a[i]//c
    remain = a[i]%c

    answer+=share

    if remain !=0:
        answer+=1

print(answer)