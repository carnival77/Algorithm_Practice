# 현재 건물이 규격에 맞는 지 확인
def possible(answer,x,y,a):
    for _ in answer:
        if a == 0:
            if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            else:
                return False
        elif a==1:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ( [x+1,y,1] in answer and [x-1,y,1] in answer ):
                continue
            else:
                return False
    return True

def solution(n, build_frame):

    answer=[]

    for order in build_frame:
        x,y,a,b = order
        if b == 1:
            answer.append([x, y, a])
            if not possible(answer, x,y,a) :
                answer.remove([x,y,a])
        elif b==0:
            answer.remove([x, y, a])
            if not possible(answer,x,y,a):
                answer.append([x, y, a])


    return sorted(answer)


prob1_n = 5
prob1_bf = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

print(solution(prob1_n,prob1_bf))