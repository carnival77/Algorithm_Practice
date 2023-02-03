n=int(input())
a=list(map(int,input().split()))
d=a # 수열 a의 각 인덱스까지의 최대 연속합을 담는다.

for i in range(1,n):
    if d[i]<d[i]+d[i-1]:
        d[i]=d[i]+d[i-1]

print(max(d))