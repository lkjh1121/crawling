from bs4 import BeautifulSoup
import requests

url = "http://www.pythonscraping.com/exercises/exercise1.html"

response = requests.get( url )
if response.status_code!=200:
    print(response.status_code, "문서 로딩 실패")
    exit() #프로그램 종료 

content = response.content
#print( content )
#이 문서로 파싱작업을 한다
 
soup = BeautifulSoup(content, 'html.parser')
#print( soup )
print( "태그", soup.title )
print( "내용만", soup.title.text )

#태그를 그냥 사용하면 되는데 동일한 문서내에 태그가 여러개일때 쓸모없음
print( soup.h1 )
print( soup.h1.text )

print( soup.div )
print( soup.div.text )

#find("태그", "속성을 이용해서") : 데이터 첫번째거 하나만 
#findall("태그", "속성을 이용해서") : 언제나 배열로 가져온다.

print( soup.find("h1").text)
print( soup.findAll("h1")[0].text) #인덱스 생략 불가 

print( soup.find("div").text)
print( soup.findAll("div")[0].text) #인덱스 생략 불가 










