from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0

    cur=0 # 현재 무게

    q=deque()

    for x in truck_weights:
        while True:
            if not q:
                q.append(x)
                cur+=x
                answer += 1
                break
            elif bridge_length == len(q):
                cur-=q.popleft()
            else:
                if cur+x <= weight:
                    q.append(x)
                    cur+=x
                    answer += 1
                    break
                else:
                    q.append(0)
                    answer += 1

    return answer + bridge_length