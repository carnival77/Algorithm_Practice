from itertools import permutations

k=int(input())
arr=list(input().split())
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

# def good(op,x,y):
#     if op=='<' and x<y:
#         return True
#     if op=='>' and x>y:
#         return True
#     return False

a=list(i for i in range(10))
for permu in permutations(a,k+1):
    permu=list(permu)
    if check(arr,permu):
        ans.append("".join(map(str,permu)))
ans.sort()
print(ans[-1])
print(ans[0])