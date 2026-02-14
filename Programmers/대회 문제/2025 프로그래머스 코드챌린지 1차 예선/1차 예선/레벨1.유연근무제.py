from collections import deque

def convert_time(time):
    h=time//100
    m=time%100
    total_minute=h*60+m
    return total_minute

def solution(schedules, timelogs, startday):
    answer = 0

    n=7
    s=startday-1

    deadlines=[]
    for schedule in schedules:
        deadlines.append(convert_time(schedule)+10)

    result=[]

    for inx,timelog in enumerate(timelogs):
        ok=True
        timelog=deque(timelog)
        timelog.rotate(s)
        timelog=list(timelog)
        deadline=deadlines[inx]
        for time in timelog[:5]:
            if convert_time(time)<=deadline:
                continue
            else:
                ok=False
                break
        if ok:
            result.append(inx)
            answer+=1

    # print(result)
    return answer

schedules = [700, 800, 1100]
# schedules = [730, 855, 700, 720]
timelogs=[[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]]
# timelogs=[[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]]
startday=5
# startday=1
print(solution(schedules,timelogs,startday))