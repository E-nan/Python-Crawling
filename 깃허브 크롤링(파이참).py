import urllib.request
from bs4 import BeautifulSoup

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

def del_space(data1, data2):
    a = ''.join(data1.split())
    b = ''.join(data2.split())
    data = {a:b}
    return data


def rep_num():
    try:
        xmlsoup = url_res(url)
        name = url.split('/')
        pagePart = xmlsoup.find('ol', {'class': 'd-flex flex-wrap list-style-none gutter-condensed mb-4'})
        anchorNumber = pagePart.find_all({'li': 'class'})
        number = len(anchorNumber)
        print(name[3] + ' 님의 Repository 개수 : ', number)

        test = pagePart.find_all('li')
        for alist in test:
            rep_name = alist.find('a').text
            rep_info = alist.find('p').text
            results = del_space(rep_name, rep_info)
            print(results)

    except:
        print('유효하지 않은 링크입니다.')


if __name__ == '__main__':
    url1 = 'http://github.com/'
    url2 = input('깃허브 아이디를 입력해주세요. : ')
    url = url1 + url2

    rnum = rep_num()