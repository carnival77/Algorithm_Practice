n=int(input())

nums=list(map(int,input().split()))

ops = list(map(int,input().split()))

max_ans=-1000000001
min_ans=10000000001

def dfs(index,s):
    global max_ans,min_ans
    # 종료 조건
    if index==n:
        # if s>=max_ans:
        #     max_ans=s
        # if s<=min_ans:
        #     min_ans=s
        max_ans = max(s,max_ans)
        min_ans = min(s,min_ans)
        return
    if index>n:
        return

    # 더하기
    if ops[0] > 0:
        ops[0]-=1
        dfs(index+1,s+nums[index])
        ops[0]+=1
    # 빼기
    if ops[1] > 0:
        ops[1]-=1
        dfs(index+1,s-nums[index])
        ops[1]+=1
    # 곱하기
    if ops[2] >0:
        ops[2]-=1
        dfs(index+1,s*nums[index])
        ops[2]+=1
    # 나누기
    if ops[3]>0 :
        ops[3]-=1
        if s<0:
            s=-s
            s//=nums[index]
            s=-s
        else:
            s//=nums[index]
        dfs(index+1,s)
        ops[3]+=1

dfs(1,nums[0])

print(max_ans)
print(min_ans)