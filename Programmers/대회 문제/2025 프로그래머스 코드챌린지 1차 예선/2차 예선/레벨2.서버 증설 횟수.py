import math

def solution(players, m, k):
    ans=0

    cur=0
    off=dict()
    debug=[]

    for time,p in enumerate(players):
        on_cnt = 0
        try:
            if off[time]>0:
                on_cnt=off[time]
                cur-=on_cnt
        except:
            pass
        need=math.floor(p/m)
        if cur<need:
            on_cnt=need-cur
            ans+=on_cnt
            cur=need
            off[time+k]=on_cnt

        debug.append([time,p,cur,on_cnt,ans])

    # for i in range(24):
    #     print(debug[i])

    return ans

# players = [0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5]
# players = [0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0]
players = [0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
# m=3
# m=5
m=1
# k=5
# k=1
k=1
print(solution(players,m,k))