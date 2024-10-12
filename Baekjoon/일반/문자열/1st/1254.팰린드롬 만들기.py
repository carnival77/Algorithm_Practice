# [풀이 시간]
# 1회 : 약 1시간 40분. 질문 게시판 반례 참고 'abcabcabc'

s=input()
p=''
n=len(s)
a=''
ok=False
if list(s)==list(s)[::-1]:
    print(len(s))
    ok=True

if not ok:
    for inx in range(n):
        front=s[inx]
        p=front+p
        a=s+p
        x=list(a)
        y=x[::-1]
        if x==y:
            break

    # print("".join(list(a)))
    print(len(a))