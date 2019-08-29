import urllib.request
from bs4 import BeautifulSoup

url = 'https://github.com/E-nan'

#해당 링크 응답함수
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
    xmlsoup = url_res(url)
    pagePart = xmlsoup.find('ol', {'class': 'd-flex flex-wrap list-style-none gutter-condensed mb-4'})
    anchorNumber = pagePart.find_all({'la': 'class'})
    number = len(anchorNumber)
    print(number)


if __name__ == '__main__':
    xmlsoup = url_res(url)
    pagePart = xmlsoup.find('ol',{'class':'d-flex flex-wrap list-style-none gutter-condensed mb-4'})
    rep_name = pagePart.find({'a':'href'}).text
    rep_info = pagePart.find({'p':'class'}).text

    result = del_space(rep_name, rep_info)
    print(result)
    rep_num()

