import sys
input=sys.stdin.readline

n=int(input())
a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))

a.sort(key=lambda x:(x[1],x[0]))
ans=1
pre_finish=a[0][1]

a.remove(a[0])

for start,end in a:
    if start<pre_finish:
        continue
    else:
        pre_finish=end
        ans+=1

print(ans)