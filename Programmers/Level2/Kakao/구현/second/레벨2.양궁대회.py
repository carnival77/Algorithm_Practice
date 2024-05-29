from itertools import combinations_with_replacement

def solution(n, info):

    a=info
    arr=[i for i in range(11)]
    cand=[]
    for comb in combinations_with_replacement(arr,n):
        b=[0]*11
        asum=0
        bsum=0
        for x in comb:
            b[x]+=1
        for i,[x,y] in enumerate(zip(a,b)):
            if (x,y)==(0,0):
                continue
            elif x<y:
                bsum+=10-i
            else:
                asum+=10-i
        if bsum>asum:
            cand.append([bsum-asum,b])
    if len(cand)==0:
        return [-1]
    cand.sort(key=lambda x:(-x[0],-x[1][10],-x[1][9],-x[1][8],-x[1][7],-x[1][6],-x[1][5],-x[1][4],-x[1][3],-x[1][2],-x[1][1],-x[1][0]))
    ans=cand[0][1]

    return ans

# n=5
# n=9
n=10
# info=[2,1,1,1,0,0,0,0,0,0,0]
# info=[0,0,1,2,0,1,1,1,1,1,1]
info=[0,0,0,0,0,0,0,0,3,4,3]
print(solution(n,info))