k=int(input())
arr=list(input().split())
used=[False]*10
ans=[]

def check(arr,num):
    for i in range(k):
        if arr[i]=='<':
            if not int(num[i])<int(num[i+1]):
                return False
        if arr[i]=='>':
            if not int(num[i])>int(num[i+1]):
                return False
    return True

def good(op,x,y):
    if op=='<' and x<y:
        return True
    if op=='>' and x>y:
        return True
    return False

def recur(index,num):
    if index==k+1:
        if check(arr,num):
            ans.append(num)
            return

    for i in range(10):
        if used[i]:
            continue
        if index==0 or good(arr[index-1],int(num[index-1]),i):
            used[i]=True
            recur(index+1,num+str(i))
            used[i]=False
recur(0,'')
ans.sort()
print(ans[-1])
print(ans[0])