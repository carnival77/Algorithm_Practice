def get_time(time):
    h=int(time[:2]) * 3600
    m=int(time[3:5]) * 60
    s=int(time[6:8])
    ms=int(time[9:])
    return (h+m+s) * 1000 + ms

def get_start_time(time,duration_time):
    n_time=duration_time[:-1]
    int_duration_time = int(float(n_time) * 1000)
    return get_time(time) - int_duration_time + 1

def solution(lines):
    answer=0
    start_time = []
    end_time=[]

    for line in lines:
        time = line.split(" ")
        start_time.append(get_start_time(time[1],time[2]))
        end_time.append(get_time(time[1]))

    for i in range(len(lines)):
        cnt=0
        cur_end_time = end_time[i]

        for j in range(i,len(lines)):
            if cur_end_time > start_time[j] - 1000:
                cnt+=1
        answer = max(answer,cnt)

    return answer

# 참고 풀이
# https://velog.io/@mrbartrns/%ED%8C%8C%EC%9D%B4%EC%8D%AC-1%EC%B0%A8%EC%B6%94%EC%84%9D-%ED%8A%B8%EB%9E%98%ED%94%BD-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A0%88%EB%B2%A83