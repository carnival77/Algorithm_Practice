# def solution(S):
#     # Implement your solution here
#     res=""
#     n=len(S)
#     a=S
#     ans=0
#
#     for i in range(n-2):
#         if a[i]<=a[i+1]:
#             res+=a[i]
#
#     if res[-1]<=a[n-2]:
#         res+=a[n-2]
#     if res[-1]<=a[n-1]:
#         res+=a[n-1]
#
#     ans=n-len(res)
#     return ans
import bisect
from bisect import bisect_right

def solution(S):

    ans=0
    dp=[]

    for ch in S:
        pos = bisect.bisect_right(dp,ch)
        if pos==len(dp):
            dp.append(ch)
        else:
            dp[pos]=ch

    ans=len(S)-len(dp)

    print(dp)

    return ans

S="banana"
print(solution(S))