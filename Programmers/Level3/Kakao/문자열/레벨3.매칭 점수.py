# from collections import defaultdict
# import re
#
# def solution(word, pages):
#     word=word.lower()
#     answer=[]
#     d=defaultdict(float)
#
#     for i,p in enumerate(pages):
#         p=p.lower()
#         #url
#         inx1=p.find("https://")
#         inx3=p.find('/>')-1
#         url=p[inx1:inx3]
#
#         #body
#         inx4=p.find('<body>')
#         inx5=inx4+len('<body>\n')
#         inx6=p.find('</body>')-1
#         body=p[inx5:inx6]
#
#         text=''
#         list_text=[]
#         if '<a href' not in body:
#             text=body
#         else:
#             link_cnt=p.count('<a href')
#             hrefs=['']*link_cnt
#             # href
#             hrefs_tmp=body[:]
#             text_tmp=body[:]
#             for i in range(link_cnt):
#                 inx7 = hrefs_tmp.find('<a href=')
#                 inx8 = hrefs_tmp.find('</a>')+len('</a>')
#                 link=hrefs_tmp[inx7:inx8]
#                 inx9=link.find('https://')
#                 inx10=link.find("></a>")
#                 href=link[inx9:inx10]
#                 hrefs[i]=href
#                 hrefs_tmp=re.sub(link,"",hrefs_tmp)
#                 text_tmp=re.sub(link,"",text_tmp)
#             # text
#             text=re.sub(r"[^a-zA-Z]", " ", text_tmp)
#             list_text=list(text.split(' '))
#         # 기본 점수
#         basic_score = list_text.count(word)
#         d[url] += basic_score
#         # 링크 점수
#         link_score = basic_score / link_cnt
#         for href in hrefs:
#             if href in d.keys():
#                 d[href] += link_score
#     min_value=-int(1e9)
#     for inx,v in enumerate(d.values()):
#         if min_value<v:
#             min_value=v
#             answer=inx
#     return answer

# solution fr
# 1. https://velog.io/@ckstn0778/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-42893%EB%B2%88-%EB%A7%A4%EC%B9%AD-%EC%A0%90%EC%88%98-X-1-Python
# 2. https://evinfor.tistory.com/31
import re

def solution(word, pages):
    webpage = []
    webpageName = []
    webpageGraph = dict()  # 나를 가리키는 외부 링크

    for page in pages:
        url = re.search('<meta property="og:url" content="(\S+)"', page).group(1)
        basicScore = 0
        for f in re.findall(r'[a-zA-Z]+', page.lower()):
            if f == word.lower():
                basicScore += 1
        exiosLink = re.findall('<a href="(https://[\S]*)"', page)

        for link in exiosLink:
            if link not in webpageGraph.keys():
                webpageGraph[link] = [url]
            else:
                webpageGraph[link].append(url)

        webpageName.append(url)
        webpage.append([url, basicScore, len(exiosLink)])  # 내가 가진 외부 링크 (개수)

    # 링크점수 = 해당 웹페이지로 링크가 걸린 다른 웹페이지의 기본점수 ÷ 외부 링크 수의 총합
    # 매칭점수 = 기본점수 + 링크점수
    maxValue = 0
    result = 0
    for i in range(len(webpage)):
        url = webpage[i][0]
        score = webpage[i][1]

        if url in webpageGraph.keys():
            # 나를 가리키는 다른 링크의 기본점수 ÷ 외부 링크 수의 총합을 구하기 위해
            for link in webpageGraph[url]:
                a, b, c = webpage[webpageName.index(link)]
                score += (b / c)

        if maxValue < score:
            maxValue = score
            result = i

    return result

word="blind"
# word="Muzi"
pages=["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
# pages=["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution(word,pages))