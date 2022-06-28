from collections import deque

def solution(progresses, speeds):
    answer=[]
    q=deque()

    for i,j in zip(progresses, speeds):
        q.append((i,j))

    while q:
        cnt=0
        for i in range(len(q)):
            if q[i][0]>=100:
                continue
            else:
                temp = q[i][0] + q[i][1]
                q[i] = (temp,q[i][1])
                if q[i][0] >= 100:
                    q[i] = (100,q[i][1])
        while True:
            try:
                first=q[0][0]
            except:
                break
            if first==100:
                cnt+=1
                q.popleft()
            else:
                break
        if cnt>0:
            answer.append(cnt)

    return answer





progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses,speeds))