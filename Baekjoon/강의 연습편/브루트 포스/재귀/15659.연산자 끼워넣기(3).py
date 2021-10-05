n=int(input())

nums=list(map(int,input().split()))

ops = list(map(int,input().split()))

max_ans=-1000000001
min_ans=10000000001

def dfs(index:int,exp:str):
    global max_ans,min_ans
    # 종료 조건
    if index==n:
        max_ans = max(eval(exp),max_ans)
        min_ans = min(eval(exp),min_ans)
        return
    if index>n:
        return

    # 더하기
    if ops[0] > 0:
        ops[0]-=1
        dfs(index+1,exp+"+"+str(nums[index]))
        ops[0]+=1
    # 빼기
    if ops[1] > 0:
        ops[1]-=1
        dfs(index+1,exp+"-"+str(nums[index]))
        ops[1]+=1
    # 곱하기
    if ops[2] >0:
        ops[2]-=1
        dfs(index+1,exp+"*"+str(nums[index]))
        ops[2]+=1
    # 나누기
    if ops[3]>0 :
        ops[3]-=1
        dfs(index+1,exp+"//"+str(nums[index]))
        ops[3]+=1

dfs(1,str(nums[0]))

print(max_ans)
print(min_ans)