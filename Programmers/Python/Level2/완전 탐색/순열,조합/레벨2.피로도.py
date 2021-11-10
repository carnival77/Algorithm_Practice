used=[]
n=0
answer=0

def dfs(cnt,k,dun):
    global answer

    if cnt > answer:
        answer = cnt

    for i in range(n):
        if dun[i][0] <= k and not used[i]:
            used[i]=True
            dfs(cnt+1,k-dun[i][1],dun)
            used[i]=False

def solution(k, dungeons):
    global n,used
    n=len(dungeons)
    used=[False]*n

    dfs(0,k,dungeons)

    return answer


k=80
dungeons = [[80,20],[50,40],[30,10]]
print(solution(k,dungeons))

from itertools import permutations

def solution2(k,dungeons):
    permu = permutations(dungeons,len(dungeons))
    cnt=0
    answer=[]

    for p in permu:
        cnt=0
        t=k
        for i in range(len(p)):
            if t>=p[i][0]:
                t-=p[i][1]
                cnt+=1
                if cnt == len(p):
                    answer.append(cnt)
                    break
            else:
                answer.append(cnt)
                break

    return max(answer)

k=80
dungeons = [[80,20],[50,40],[30,10]]
print(solution2(k,dungeons))