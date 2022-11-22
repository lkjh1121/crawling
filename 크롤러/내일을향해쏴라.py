from bs4 import BeautifulSoup
import requests 
url="https://ko.wikipedia.org/wiki/%EB%82%B4%EC%9D%BC%EC%9D%84_%ED%96%A5%ED%95%B4_%EC%8F%B4%EB%9D%BC"
response = requests.get(url)
print( response.status_code )

content = response.content
soup = BeautifulSoup(content, "html.parser") 
title = soup.find("span", {"class":"mw-page-title-main"})
print(title.text)

#태그 선택후 - 마우스 오른쪽  - copy selector
selector="#mw-content-text > div.mw-parser-output > p:nth-child(4)"
temp = soup.select(selector)
print( type(temp))
print( temp[0].text  )

tempList=[]
for i in range(8, 12):
    s = f"#mw-content-text > div.mw-parser-output > p:nth-child({i})"
    temp = soup.select(s)
    tempList.append( temp[0].text)

s="\n"
s = s.join(tempList) #list에 있는걸 하나의 문자열로 모두 합쳐준다
print( s )

#파일에 저장하기 
f = open("test.txt", "w", encoding="utf-8")
print(s, file=f) #출력위치가 파일이다
f.close()








