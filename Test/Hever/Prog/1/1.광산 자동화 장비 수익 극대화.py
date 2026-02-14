import math

dp=[]
n=0
total_time=0

def process(level,cost,use_time,gold,upgrades):
    global dp,n,total_time

    goal_level=level+1
    r_time,r_money=dp[level]

    goal_money=upgrades[goal_level][0]

    if goal_money<=r_money:
        r_money-=goal_money
    else:
        goal_cnt=math.ceil((goal_money-r_money)/gold)
        total_use_time=use_time*goal_cnt
        if r_time>=total_use_time:
            r_time-=total_use_time
            r_money=r_money+gold*goal_cnt-goal_money
        else:
            return

    dp[level+1]=[r_time,r_money]

def solution(T,upgrades):
    global dp,n,total_time

    ans=0
    total_time=T
    n=len(upgrades)
    dp=[[-1,-1] for _ in range(n)] # level i로 업그레이드하고 남은 시간과 돈
    dp[0]=[T,0]
    upgrade=upgrades[:-1]

    for level,[cost,use_time,gold] in enumerate(upgrade):
        process(level,cost,use_time,gold,upgrades)

    for level,[cost,use_time,gold] in enumerate(upgrades):
        earn=0
        r_time,r_money=dp[level]
        if r_time>0:
            cnt=r_time//use_time
            earn+=cnt*gold+r_money
            ans=max(earn,ans)

    return ans

# 1
# T=100
# upgrades=[[0,10,30],[100,5,50],[200,2,100]]
# result=2020

# 2
# T=50
# upgrades=[[0,10,30],[100,5,50]]
# result=150

# 3
# T=1000
# upgrades=[[0,20,50],[520,10,100],[1050,5,500]]
# result=67080

# 4
# T=10
# upgrades=[[0,100,10],[0,50,5]]
# result=0

# 5
# T=100
# upgrades=[[0,1,1],[10000,1,100]]
# result=100

# 6
# T=3
# upgrades=[[0,5,100],[0,4,1000],[0,10,99999]]
# result=0

# 7
# T=9
# upgrades=[[0,4,5],[9,3,100]]
# result=10

# 8
# T=30
# upgrades=[[0,10,1],[100,1,1000]]
# result=3

print(solution(T,upgrades))