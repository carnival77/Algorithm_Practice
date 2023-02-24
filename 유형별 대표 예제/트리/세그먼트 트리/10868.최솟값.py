import sys
input=sys.stdin.readline

n,m=map(int,input().split())
treeHeight=0
length=n

while length!=0:
    length//=2
    treeHeight+=1

treeSize=pow(2,treeHeight+1)
leftNodeStartIndex=treeSize//2-1
tree=[sys.maxsize]*(treeSize+1)

for i in range(leftNodeStartIndex+1,leftNodeStartIndex+n+1):
    tree[i]=int(input())

def setTree(i):
    while i!=1:
        if tree[i//2]>tree[i]:
            tree[i//2]=tree[i]
        i-=1

setTree(treeSize-1)

def getMin(s,e):
    Min=sys.maxsize
    while s<=e:
        if s%2==1:
            Min=min(Min,tree[s])
            s+=1
        if e%2==0:
            Min=min(Min,tree[e])
            e-=1
        s//=2
        e//=2
    return Min

for _ in range(m):
    s,e=map(int,input().split())
    s+=leftNodeStartIndex
    e+=leftNodeStartIndex
    print(getMin(s,e))