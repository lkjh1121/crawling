from bs4 import BeautifulSoup
import requests 
import pandas as pd 

base_url = "https://www.navercorp.com/investment/stock"
param="daySiseCurrentPage=5&timeSiseCurrentPage=4&pageAction=DayPage"

def crawling(pageCnt=10):
    for page in range(1,  pageCnt+1):
        params ={"daySiseCurrentPage":page, 
                "timeSiseCurrentPage":4, 
                "pageAction":"DayPage"}

        response = requests.get(base_url, params=params)
        #response.status_code : 문서를 불러오는걸 성공했을 경우 200
        print( response.status_code )
        if response.status_code!=200:
            print("페이지 로드 실패")
            return #exit() -> return 
        #불러온 문서로부터 태그를 제거하고 원하는 데이터를 추출해야 한다(파싱)
        #response.content 에 불러온 문서 내용이 있음
        bs = BeautifulSoup( response.content, "html.parser")

        table = bs.find("table", {"class":"investors_table type2 bt0"})

        if page==1:
            df = pd.DataFrame()
        
        tbody = table.find("tbody")
        tr_list  = tbody.find_all("tr")
        for tr in tr_list:
            temp = dict()
            i=1
            for td in tr.find_all("td"):
                #print( td.text, end=" ")
                temp[f"col{i}"]=td.text
                i=i+1
            df = df.append( temp, ignore_index=True )

        print( df )


