import sys
from itertools import product
input=sys.stdin.readline

a=list(map(int,input().split()))
h=[0,1,2,3]
ans=0
end=32

blue=dict() # 파란색 루트 탈 경우의 이전(key) - 이후(value) 연결
red=dict() # 빨간색 루트만 탈 경우의 이전(key) - 이후(value) 연결

for i in range(20):
    red[i]=i+1
red[20]=end

blue[5]=21
blue[21]=22
blue[22]=23
blue[23]=29
blue[10]=24
blue[24]=25
blue[25]=29
blue[15]=26
blue[26]=27
blue[27]=28
blue[28]=29
blue[29]=30
blue[30]=31
blue[31]=20
blue[20]=end

score=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,13,16,19,22,24,28,27,26,25,30,35,0]

def move(num,no):
    global pos

    now=pos[no]
    if now in (5,10,15):
        colors[no]=1
    color = colors[no]
    if color==0:
        route=red
    else:
        route=blue
    for i in range(num):
        # 말이 도착 칸으로 이동하면 주사위에 나온 수와 관계 없이 이동을 마친다.
        if now==end:
            break
        now=route[now]
    # 말이 이동을 마치는 칸에 다른 말이 있으면 그 말은 고를 수 없다. 단, 이동을 마치는 칸이 도착 칸이면 고를 수 있다.
    if now in pos and now!=end:
        return -1
    else:
        pos[no]=now
        return score[now]

# 게임은 10개의 턴으로 이루어진다. 매 턴마다 1부터 5까지 한 면에 하나씩 적혀있는 5면체 주사위를 굴리고,
for prod in product(h,repeat=10):
    point=0
    prod=list(prod)
    # 처음에는 시작 칸에 말 4개가 있다.
    pos = [0] * 4 # 말별 위치. 0은 시작지점, 32는 도착지점(end)
    # 말은 게임판에 그려진 화살표의 방향대로만 이동할 수 있다.
    # 말이 파란색 칸에서 이동을 시작하면 파란색 화살표를 타야 하고, 이동하는 도중이거나 파란색이 아닌 칸에서 이동을 시작하면 빨간색 화살표를 타야 한다
    colors=[0]*4 # 말별 루트. 0이면 레드, 1이면 블루
    ok=True
    for num,no in zip(a,prod):
        # 도착 칸에 있지 않은 말을 하나 골라 주사위에 나온 수만큼 이동시킨다.
        if pos[no]==end:
            ok=False
            break
        # 말이 이동을 마칠 때마다 칸에 적혀있는 수가 점수에 추가된다.
        res=move(num,no)
        if res==-1:
            ok=False
            break
        else:
            point+=res
    if ok:
        ans=max(ans,point)
print(ans)