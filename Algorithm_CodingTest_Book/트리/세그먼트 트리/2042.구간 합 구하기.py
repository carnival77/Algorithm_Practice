import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
treeHeight=0
length=n

# 트리의 높이 구하기. 리프 노드의 개수를 2씩 나누어 가면서 높이 계산
while length!=0:
    length//=2
    treeHeight+=1

treeSize=pow(2,treeHeight+1)
# 리프 노드 시작 인덱스
leftNodeStartIndex=treeSize//2-1
tree=[0]*(treeSize+1)

# tree 리스트의 리프 노드 영역에 데이터 입력
for i in range(leftNodeStartIndex+1,leftNodeStartIndex+n+1):
    tree[i]=int(input())

# 인덱스 트리 생성 함수
def setTree(i):
    # 인덱스가 루트가 아닐 때까지
    while i!=1:
        # 부모 노드(인덱스/2)에 현재 인덱스의 트리값 더하기
        tree[i//2]+=tree[i]
        i-=1

# 초기 트리 생성
setTree(treeSize-1)

# 값 변경 함수
def changeVal(index,value):
    # 현재 노드 값과 변경할 값의 차이
    diff=value-tree[index]
    # 시작 인덱스가 0보다 클 경우 지속
    while index>0:
        # 시작 인덱스 트리값에 diff 더함
        tree[index]=tree[index]+diff
        # 시작 인덱스 = 시작 인덱스 / 2
        index=index//2

# 구간 합 계산 함수
def getSum(s,e):
    partSum=0
    while s<=e:
        if s%2==1:
            partSum+=tree[s]
            s+=1
        if e%2==0:
            partSum+=tree[e]
            e-=1
        s//=2
        e//=2
    return partSum

for _ in range(m+k):
    q,s,e=map(int,input().split())
    if q==1:
        changeVal(leftNodeStartIndex+s,e)
    else:
        s+=leftNodeStartIndex
        e+=leftNodeStartIndex
        print(getSum(s,e))