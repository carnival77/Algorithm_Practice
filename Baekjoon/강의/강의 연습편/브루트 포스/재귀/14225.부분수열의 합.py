# from itertools import combinations

# 시도 2 : 가능한 부분수열의 개수만큼 boolean 배열 c를 선언. 가능한 모든 부분수열의 합을 c에 체크
n=int(input())

nums=list(map(int,input().split()))

c=[False]*(n*100000+10)

def go(index,s):
    if index==n:
        c[s] = True
        return
    go(index+1,s+nums[index])
    go(index+1,s)

go(0,0)
ans=1
while True:
    if c[ans] == False:
        break
    ans+=1
print(ans)

# arr=[]

# 시도 1 : combinations, boolean 배열 사용 X : 시간 초과.
# for i in range(1,n+1):
#     for j in combinations(arr,i):
#         sums.append(sum(j))

# def go(index,s):
#     if index==n:
#         sums.append(s)
#         return
#     go(index+1,s+nums[index])
#     go(index+1,s)
#
# go(0,0)
#
# # 이 부분이 시간 초과. sums의 최대 크기는 2의 20승 ( 약 1백만 ). 자연수의 최대 크기는 2백만이므로, 두 개의 곱은 20억이 넘는다. 따라서 시간 초과
# while ans<2000001:
#     if not ans in sums:
#         break
#     else:
#         ans+=1
#
# print(ans)

