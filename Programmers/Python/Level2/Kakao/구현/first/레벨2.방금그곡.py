def solution(m, musicinfos):
    answer = ''
    result=[]

    M=m.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a")

    for index,musicinfo in enumerate(musicinfos):
        start, end, title, song = musicinfo.split(",")
        hour,minute=map(int,start.split(":"))
        start_time=hour*60+minute
        hour,minute=map(int,end.split(":"))
        end_time=hour*60+minute
        play_time=end_time-start_time

        song = song.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace(
            "A#", "a")

        song_len=len(song)
        s,r=play_time//song_len,play_time%song_len
        played_Song=song*s+song[:r]
        Ml=len(M)
        for i in range(len(played_Song)-Ml+1):
            if played_Song[i:i+Ml]==M:
                result.append([title,play_time,index])

    if len(result)>=2:
        result.sort(key=lambda x:(-x[1],x[2]))
        answer=result[0][0]
        return answer
    elif len(result)==1:
        answer=result[0][0]
        return answer
    else:
        return "(None)"

# m="ABCDEFG"
# m="CC#BCC#BCC#BCC#B"
m="ABC#"
# m="ABC#"
# musicinfos=["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# musicinfos=["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
# musicinfos=["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# musicinfos=["12:00,12:05,A,GABC#","12:00,12:05,B,GABCG"]
musicinfos=["12:00,12:05,A,GABC#","12:00,12:04,B,GABC"]
print(solution(m,musicinfos))