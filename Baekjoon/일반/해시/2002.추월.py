n=int(input())
d1,d2=dict(),dict()
for i in range(n):
    d1[input()]=i
for i in range(n):
    d2[input()]=i
ans=0
s=set()
for k in d2.keys():
    if d1[k]>d2[k]:
        s.add(k)

for front in d2.keys():
    for back in d2.keys():
        if d2[front]>=d2[back]: continue
        if d1[front]>d1[back] and front not in s:
            s.add(front)
ans=len(s)
print(ans)

# 추가 예제
# 6
# 1
# 2
# 3
# 4
# 5
# 6
# 2
# 4
# 3
# 1
# 6
# 5