import urllib.request
from bs4 import BeautifulSoup
# import os   #환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈
# import sys #파이썬 파일을 실행할 때, 자기 자신의 파일명이 들어간다
# import datetime #날짜관련 모듈
# import csv

url = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=102&sid2=250&listType=title'


# 사용자가 년도와 월을 입력할 경우
def DateNum(mon):
    mon = int(mon)

    if mon % 2 != 0 and mon < 8 or mon % 2 == 0 and mon > 7:
        return 31
    elif mon == 2:  # 2월의 날짜는 혼자다름
        return 28
    elif mon % 2 == 0 and mon < 7 or mon % 2 != 0 and mon > 8:
        return 30

def url_res(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    #print(rescode)
    if(rescode==200):
        response_body = response.read()
        xmlsoup = BeautifulSoup(response_body,'html.parser')
        return xmlsoup
    else:
        return None

# 사용자가 원하는 월을 입력받아 원하는 월의 기사만 추출
def newspage(mon):
    if mon < 10:  # 월이 10 이하일 경우 앞에 0 추가
        Adate = '0' + str(mon)
    else:
        Adate = str(mon)

    days = DateNum(mon)  # 각 월에 해당하는 날짜 추출
    for days in range(1, days, 1):
        if days < 10:  # 날짜가 10 이하일경우 앞에 0 추가
            Bdate = '0' + str(days)
        else:  # 그외 날짜는 그대로 저장
            Bdate = str(days)
        date = '2019' + str(Adate) + str(Bdate)
        url_date = url + '&date=' + date
        print(url_date)

        xmlsoup = url_res(url_date)
        pagePart = xmlsoup.find('div', {'class': 'paging'})
        anchorNumber = pagePart.find_all({'a': 'href'})
        pageNumber = len(anchorNumber) + 1

        if (pageNumber == 11):
            imsiUrl = url_date + '&page=11'
            xmlsoup = url_res(imsiUrl)
            pagePart = xmlsoup.find('div', {'class': 'paging'})
            anchorNumber = pagePart.find_all({'a': 'href'})
            pageNumber = len(anchorNumber) + 10
        print("페이지수", pageNumber)

        for page in range(1, pageNumber + 1, 1):  # 해당 날의 모든 페이지 링크를 추출
            newDayUrl = url_date + '&page=' + str(page)
            # print(newDayUrl) #각 페이지별 링크
            # print(page)      #page번째 페이지
            xmlsoup = url_res(newDayUrl)
            listBody = xmlsoup.find('div',{'class':'list_body'})
            allList = listBody.findAll('li')
            for alist in allList:
                Title = alist.find('a').text
                # fresult = Search_Subject(Title)

#현재 모듈의 이름을 담고 있는 내장변수
#직접 실행하면 if문 실행되지만 다른 프로그램에서 import하면 if문 실행x

if __name__=='__main__':
    year = input("년도 : ")
    Amon = input("월 : ")
    Bmon = input("월 : ")

    print(Amon + "월 부터 " + Bmon + "월 까지의 기사 링크")
    for mon in range(int(Amon), int(Bmon) + 1, 1):
        print(mon, '월')
        newspage(mon)