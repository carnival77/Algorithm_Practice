import sys
from itertools import permutations
input=sys.stdin.readline

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
arr=[1,2,3,4,5,6,7,8]
ans=0

def move(x):
    global one,two,three,point

    if x==1:
        if three==1:
            three=0
            point+=1
        if two==1:
            three=1
            two=0
        if one==1:
            two=1
            one=0
        one=1
    elif x==2:
        if three==1:
            three=0
            point+=1
        if two==1:
            two=0
            point+=1
        if one==1:
            three=1
            one=0
        two=1
    elif x==3:
        if three==1:
            three=0
            point+=1
        if two==1:
            two=0
            point+=1
        if one==1:
            one=0
            point+=1
        three=1
    else:
        if three==1:
            three=0
            point+=1
        if two==1:
            two=0
            point+=1
        if one==1:
            one=0
            point+=1
        point+=1

for perm in permutations(arr,8):
    point = 0
    b = list(perm)
    b.insert(3, 0)
    i = 0
    for eaning in range(n):
        result=a[eaning]
        out = 0
        one,two,three=0,0,0
        while True:
            no=b[i]
            res=result[no]
            if res==0:
                out+=1
            else:
                move(res)
            i+=1
            if i==9:
                i=0
            if out == 3:
                break
    ans=max(ans,point)
print(ans)