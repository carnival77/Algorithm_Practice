import sys
input=sys.stdin.readline

nums=list(map(int,input().split())) # 주사위 숫자들

n = 33 # 칸의 총 개수. 도착 지점 인덱스 = n-1
score = [
    0,2,4,6,8,
    10,13,16,19,25,
    12,14,16,18,20,
    22,24,22,24,26,
    28,26,27,28,30,
    32,34,36,38,30,
    35,40,0
]

# 칸 배열. 같은 숫자라고 하더라도 인덱스가 다르기에 다른 칸으로 취급된다. a[i]는 다음 칸의 인덱스를 저장하고 있다.
a = [0]*n
# a[i][0] : i에서 이동을 시작. a[i][1] : i를 지나갈 때
a[0] = [1,1]
a[1] = [2,2]
a[2] = [3,3]
a[3] = [4,4]
a[4] = [5,5]
a[5] = [6,10]
a[6] = [7,7]
a[7] = [8,8]
a[8] = [9,9]
a[9] = [29,29]
a[10] = [11,11]
a[11] = [12,12]
a[12] = [13,13]
a[13] = [14,14]
a[14] = [15,17]
a[15] = [16,16]
a[16] = [9,9]
a[17] = [18,18]
a[18] = [19,19]
a[19] = [20,20]
a[20] = [24,24]
a[21] = [9,9]
a[22] = [21,21]
a[23] = [22,22]
a[24] = [23,25]
a[25] = [26,26]
a[26] = [27,27]
a[27] = [28,28]
a[28] = [31,31]
a[29] = [30,30]
a[30] = [31,31]
a[31] = [32,32]

# 이동할 칸의 인덱스 반환
def move(num,start):
    now=start
    for i in range(num):
        if now == n - 1:  # 도착 칸에 도달했으면 이동 중지
            break
        if i==0: # 처음 시작할 때
            now=a[now][0]
        else:
            now=a[now][1]
    return now

def process(turn,players,point):
    if turn==10:
        return point
    ans=0
    # 4개 말을 순서대로 이동시킨다.
    for i in range(4):
        next=move(nums[turn],players[i])
        # 말이 이동할 칸이 도착 칸이 아니며 그 곳에 다른 말이 있으면 이동 불가
        if next!=n-1 and next in players:
            continue
        # 이동 가능하면
        nplayers=players[:]
        nplayers[i]=next
        tmp=process(turn+1,nplayers,point+score[next])
        ans=max(ans,tmp)
    return ans

print(process(0,[0,0,0,0],0))