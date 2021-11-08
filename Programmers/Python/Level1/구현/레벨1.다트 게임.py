def solution(dartResult):
    arr=dartResult

    inx=0
    stages=[0]*3
    s_inx=-1
    bonus = ['S','D','T']
    option = ['*','#']

    while inx < len(arr):
        if arr[inx].isdigit():
            s_inx += 1
            if arr[inx] == '1' and arr[inx+1] == '0':
                stages[s_inx] = int(arr[inx:inx+2])
                print("test : ",stages)
                inx+=1
            else: stages[s_inx] = int(arr[inx])
        if arr[inx] in bonus:
            if arr[inx] == 'D':
                stages[s_inx] = stages[s_inx] ** 2
            elif arr[inx] == 'T':
                stages[s_inx] = stages[s_inx] ** 3
        if arr[inx] in option:
            if arr[inx] == '#':
                stages[s_inx] = -stages[s_inx]
            if arr[inx] == '*':
                if s_inx == 0 :
                    stages[s_inx] *= 2
                else:
                    stages[s_inx] *= 2
                    stages[s_inx-1] *= 2
        inx+=1

    return sum(stages)

dartResult = '1D2S#10S'

print("answer : ",solution(dartResult))

def solution2(dartResult):
    temp = dartResult.replace('10','k')

    arr = ['10' if i == 'k' else i for i in temp]

    i=-1
    stages=[0]*3
    s_inx=-1
    bonus = ['S','D','T']

    for ele in arr:
        if ele.isdigit():
            s_inx += 1
            stages[s_inx] = int(ele)
            continue
        elif ele in bonus:
            stages[s_inx] = stages[s_inx] ** (bonus.index(ele)+1)
            continue
        else:
            if ele == '#':
                stages[s_inx] = -stages[s_inx]
            else:
                stages[s_inx] *= 2
                if s_inx > 0:
                    stages[s_inx-1] *= 2
        print(stages)

    return sum(stages)

dartResult = '1D2S#10S'

print("answer : ",solution2(dartResult))

