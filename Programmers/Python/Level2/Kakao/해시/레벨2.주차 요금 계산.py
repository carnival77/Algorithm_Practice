import math

def change(time):
    hour,minute = time.split(":")
    return int(hour)*60 + int(minute)

def solution(fees, records):
    answer = []

    d=dict()
    check=dict() # 현재 차가 있는 지. 입차하고 출차 안 했으면 True

    for record in records:
        time,num,act = record.split(" ")
        mins=change(time)
        if act=="IN":
            try:
                d[num]=d[num]+mins
            except:
                d[num]=mins
            check[num]=True
        else:
            d[num]=d[num]-mins
            check[num]=False

    for key,val in check.items():
        if check[key]:
            d[key]=d[key]-1439

    l=[]
    for key,val in d.items():
        d[key]=abs(val)
        l.append([key,d[key]])
    l.sort(key=lambda x:x[0])

    for n,t in l:
        fee=fees[1]
        if t>fees[0]:
            fee+=math.ceil((t-fees[0])/fees[2])*fees[3]
        answer.append(fee)

    return answer

fees=[180, 5000, 10, 600]
records=["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees,records))