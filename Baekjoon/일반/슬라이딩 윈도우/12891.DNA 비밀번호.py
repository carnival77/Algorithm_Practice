import sys
input=sys.stdin.readline

s,p=map(int,input().split())
a=list(input())
ans=0
check=list(map(int,input().split()))
same=0
my=[0]*4

def my_add(c):
    global my,check,same
    if c=='A':
        my[0]+=1
        if my[0]==check[0]:
            same+=1
    elif c=='C':
        my[1]+=1
        if my[1]==check[1]:
            same+=1
    elif c=='G':
        my[2]+=1
        if my[2]==check[2]:
            same+=1
    else:
        my[3]+=1
        if my[3]==check[3]:
            same+=1

def my_remove(c):
    global my,check,same
    if c=='A':
        if my[0]==check[0]:
            same-=1
        my[0]-=1
    elif c=='C':
        if my[1]==check[1]:
            same-=1
        my[1]-=1
    elif c=='G':
        if my[2]==check[2]:
            same-=1
        my[2]-=1
    else:
        if my[3]==check[3]:
            same-=1
        my[3]-=1

for i in check:
    if i==0:
        same+=1

for i in range(p):
    my_add(a[i])

if same==4:
    ans+=1

for end in range(p,s):
    start=end-p
    my_add(a[end])
    my_remove(a[start])
    if same == 4:
        ans += 1

print(ans)