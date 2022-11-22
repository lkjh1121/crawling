from bs4 import BeautifulSoup
import requests 
from urllib.parse import quote 
import DrawCloud as dc

"""
https://search.naver.com/search.naver?where=news&sm=tab_pge&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=24&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all

검색어 쿼리 : &query=%EC%B9%B4%EC%B9%B4%EC%98%A4
페이징 쿼리 : &start=41
"""

custom_header = {
    "referer":"https://search.naver.com/search.naver?where=news",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

def makeUrl(keyword="카카오", page=1):
    base_url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=24&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all"
    query_url = "&query="+ quote(keyword)
    #1 1       (p-1)*10   +1  
    #2 11 
    #3 21 
    #4 31
    #5 41
    paging_url = f"&start={(page-1)*10+1}"
    url = base_url + query_url + paging_url
    return url 

def getTitleContents(url):
    response = requests.get(url, headers=custom_header)
    title=""
    contents=""
    if response.status_code!=200:
        return title, contents 

    content = response.content
    soup = BeautifulSoup(content, "html.parser") 
    titletag = soup.find("h2", {"class":"media_end_head_headline"})
    if titletag!=None:
        title = titletag.text 
    contenttag = soup.find("div", {"id":"newsct_article"})
    if contenttag!=None:
        contents=contenttag.text

    return title, contents 


def crawling(keyword="카카오", pageCnt=10, filename="카카오2.txt"):
    f = open(filename, "w", encoding="utf-8")
    for page in range(1, pageCnt+1):
        url = makeUrl(keyword, page)
        response = requests.get(url, headers=custom_header)
        if response.status_code !=200:
            print("작업종료")
            return 
        bs = BeautifulSoup(response.content, 'lxml') 
        news_list = bs.find_all("a", {"class":"info"})
        for news_url in news_list:            
            if "n.news.naver.com" in news_url['href']  \
                and "entertain" not in news_url['href']:
                print( news_url['href'] )
                title, contents = getTitleContents(news_url['href'] )        
                print(title, contents, file=f)
    f.close()

def getStopWords(filename="stopwords.txt"):
    f = open(filename, "r", encoding="utf8")
    stopwords = f.readlines() 
    s=[]
    for w in stopwords:
        s.append( w[0:len(w)-1])
    f.close()
    return s 

def start():
    while True:
        print("1.데이터 작성")
        print("2.워드클라우드 작성")
        print("0.종료")
        sel = input("선택 : ")
        if sel == "1":
            keyword = input("검색어 : ")
            pageCnt = int(input("페이지 개수 : "))
            filename = input("저장파일명 : ")
            crawling(keyword, pageCnt, filename)
        elif sel=="2":    
            stop_words=getStopWords()
            filename = input("읽을파일명 : ")
            dc.main(filename,stop_words,"alice_mask.png") 
        else:
            return 

if __name__ == "__main__":
    start()



