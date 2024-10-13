# [풀이 시간]
# 1회 : 약 2시간. 풀이 참고 O.

t=int(input())
for round in range(1,t+1):
    n=int(input())
    arr=[]
    for _ in range(n):
        data=input()
        row=[int(i) for i in data]
        arr.append(row)
    arr.sort()

    ok=True
    for inx in range(n-1):
        bf=arr[inx-1]
        af=arr[inx+1]
        now=arr[inx]
        bf_len=len(bf)
        af_len=len(af)
        now_len=len(now)

        tg2=af[:now_len]
        if tg2==now:
            ok=False
            break

    if ok:
        print("YES")
    else:
        print("NO")