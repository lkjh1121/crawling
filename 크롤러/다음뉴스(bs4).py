"""
https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=%EC%B9%B4%EC%B9%B4%EC%98%A4&p=4
                
w=news&DA=PGD&enc=utf8
                                                                %EC%B9%B4%EC%B9%B4%EC%98%A4         
q항목이 검색어
p항목이 페이지 
"""
from DBModule import DBModule

from urllib.parse import quote
from bs4 import BeautifulSoup
import requests 

print(  quote("카카오") )

def getUrl(keyword, page):
    base_url = "https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1"
    query = "&q="+quote(keyword)
    page = "&p=" + str(1)
    url = base_url + query + page 
    return url 

def crawling(keyword="카카오", pageCnt=5, filename="카카오.txt"):
    f = open(filename, "w", encoding="utf-8")
    db = DBModule()            
    for page in range(1, pageCnt+1):
        print(f"{page} 작업중 ------------")
        url = getUrl(keyword, page)
        response = requests.get(url)
        if  response.status_code!=200:
            print("작업종료")       
            return #함수종료

        soup = BeautifulSoup(response.content) #파싱은 종료 
        #ul태그를 가져오자, ul태그에 class 나 id가 없으면 select함수로 가져오자
        ul =  soup.find("ul", {"class":"list_news"})
        #못갖고 오면 None 
        if ul == None:
            print("못찾음")
            return  #함수를 종료하면 된다. 

        liList = ul.find_all("li")
        #print( liList )

        for li in liList:
            a = li.find("a", {"class":"f_nb"})
            if a!=None:
                print( a['href'] +" 작업중 ....")
                url2 = a['href']
                title, contents = getTitleContents(url2)
                sql="""
                insert into kakao(title, contents)
                values(%s, %s)
                """
                db.execute( sql, ( title, contents))
                print(title, contents, file=f)

    db.close() #전체 다 종료하고 
    f.close() #함수 종료시 파일 닫기 

def getTitleContents(url):
    response = requests.get(url)
    title=""
    contents=""
    if response.status_code!=200:
        return title, contents 

    content = response.content
    soup = BeautifulSoup(content, "html.parser") 
    titletag = soup.find("h3", {"class":"tit_view"})
    title = titletag.text 
    contenttag = soup.find("div", {"class":"article_view"})
    contents=contenttag.text

    return title, contents 
    

if __name__ == "__main__":
    crawling("카카오", 50, "카카오.txt")


"""
CREATE TABLE kakao(
   id BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
   title VARCHAR(100) NOT NULL,
   contents LONGTEXT NOT NULL,
   wdate DATETIME DEFAULT CURRENT_TIMESTAMP
);

"""

