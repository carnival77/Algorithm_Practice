from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0

    cur=0 # 현재 무게

    q=deque()

    for x in truck_weights:
        while True:
            answer += 1
            if not q:
                q.append(x)
                cur+=x
                break
            elif bridge_length == len(q):
                cur-=q.popleft()
            else:
                if cur+x <= weight:
                    q.append(x)
                    cur+=x
                    break
                else:
                    q.append(0)

    return answer + bridge_length