# 두 수를 곱한 결과가 두 수를 더한 결과보다 크면 곱하고(묶고),
# 아니면 묶지 않고 합산한다.
# 단, 0이 있으면 음수와 곱해서 음수를 0으로 만들어 결과값을 높일 수 있다.
n=int(input())
pos,neg,zero=[],[],0
for i in range(n):
    data=int(input())
    if data>0:
        pos.append(data)
    elif data<0:
        neg.append(data)
    else:
        zero+=1
pos.sort(reverse=True) # 양수 : 내림차순 정렬
neg.sort() # 음수 : 오름차순 정렬
i=0
ans=0
while i<len(pos):
    if i+1<len(pos) and pos[i]*pos[i+1]>pos[i]+pos[i+1]:
        ans+=pos[i]*pos[i+1]
        i+=2
    else:
        ans+=pos[i]
        i+=1
i=0
while i<len(neg):
    if i+1<len(neg) and neg[i]*neg[i+1]>neg[i]+neg[i+1]:
        ans+=neg[i]*neg[i+1]
        i+=2
    else:
        if zero>0:
            zero-=1
        else:
            ans+=neg[i]
        i+=1
print(ans)

# 추가 예제
# (1)
# 5
# -1
# -2
# -3
# -4
# -5
# 답 25
# (2)
# 7
# 3
# 2
# 1
# 0
# -3
# -2
# -1
# 답 13