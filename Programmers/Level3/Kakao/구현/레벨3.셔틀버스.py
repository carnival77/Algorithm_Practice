#!/usr/bin/env Python
# coding=utf-8
def chg(a):
    if type(a) is str:
        return int(a[:2])*60 + int(a[3:])
    else:
        res=divmod(a,60)
        hour=str(res[0])
        min=str(res[1])
        if len(hour)<2:
            hour='0'+hour
        if len(min)<2:
            min='0'+min
        return hour+":"+min

def process(n,t,m,timetable):
    for time in range(540,1440,t):
        if n==1:
            if len(timetable)<m or timetable[0]>time:
                return time
            elif len(timetable)>=m:
                return timetable[m-1]-1
        bus=[]
        for crew in timetable:
            if crew <= time:
                if len(bus)<m:
                    bus.append(crew)
                else:
                    break
        for crew in bus:
            timetable.remove(crew)
        n -= 1

def solution(n, t, m, timetable):
    timetable.sort()
    for i in range(len(timetable)):
        timetable[i]=chg(timetable[i])
    return chg(process(n,t,m,timetable))

# n=1
# n=2
# n=10
# n=10
n=3
t=1
# t=10
# t=60
# t=25
# m=5
m=2
# m=1
# m=45
# timetable=["08:00", "08:01", "08:02", "08:03"]
# timetable=["09:10", "09:09", "08:00"]
# timetable=	["00:01", "00:01", "00:01", "00:01", "00:01"]
# timetable=	["23:59"]
# timetable=	["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
# timetable=	["09:00", "09:10" ,"09:20" ,"09:30" ,"09:40" ,"09:50","10:00", "10:10" ,"10:20" ,"10:30" ,"10:40" ,"10:50"]
timetable=	["06:00", "23:59", "05:48", "00:01", "00:01"]
print(solution(n,t,m,timetable))