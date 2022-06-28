from itertools import  combinations

def solution(n, info):
    answer = []
    cond=[]
    score=[10,9,8,7,6,5,4,3,2,1,0]
    for i in info:
        cond.append(i+1)

    for i in range(1,n+1):
        for comb in combinations([0,1,2,3,4,5,6,7,8,9],i):
            a_score = 0
            l_score = 0
            res = [0]*11
            sum=0
            for j in comb:
                sum+=cond[j]
            if sum>n:
                continue
            else:
                rest=n-sum
                for j in comb:
                    l_score+=score[j]
                for index,k in enumerate(info):
                    if k!=0:
                        if index not in comb:
                            a_score+=score[index]
                if l_score>a_score:
                    dif=l_score-a_score
                    for j in comb:
                        res[j]=cond[j]
                    if rest!=0:
                        res[10]+=rest
                    answer.append((dif,res))
    if len(answer)==0:
        return [-1]
    else:
        answer.sort(key=lambda x:(-x[0],-x[1][10],-x[1][9],-x[1][8],-x[1][7],-x[1][6],-x[1][5],-x[1][4],-x[1][3],-x[1][2],-x[1][1],-x[1][0]))
        return answer[0][1]

# n=5
# n=1
# n=9
n=10
# info=[2,1,1,1,0,0,0,0,0,0,0]
# info=[1,0,0,0,0,0,0,0,0,0,0]
# info=[0,0,1,2,0,1,1,1,1,1,1]
info=[0,0,0,0,0,0,0,0,3,4,3]
print(solution(n,info))