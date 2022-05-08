def solution(files):
    n=5

    temp=[]

    for file in files:
        head=''
        index=0
        number=''
        for i,alp in enumerate(file):
            if alp.isdigit():
                head=file[:i]
                index=i
                break

        number+=file[index]
        for j in range(index+1,len(file)):
            if file[j].isdigit():
                number+=file[j]
            else:
                break

        if len(number)<n:
            zeros=n-len(number)
            tmp=''
            for _ in range(zeros):
                tmp+='0'
            number=tmp+number
        temp.append([file, head,number])

    temp.sort(key=lambda x:(x[1].lower(),x[2]))
    answer=[x[0] for x in temp]

    return answer

import re

def solution2(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b



# import re

def solution3(files):

    def key_function(fn):
        head,number,tail = re.match(r'([a-z-. ]+)(\d{,5})(.*)',fn).groups()
        return [head,int(number)]

    return sorted(files, key = lambda x: key_function(x.lower()))

# files= ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
files=["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))
