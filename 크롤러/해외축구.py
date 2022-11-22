from distutils.dep_util import newer
from bs4 import BeautifulSoup
#Ajax기술로 코딩이 되서 데이터를 json 형태로 가져온다
#BeautifulSoup 는 json 파싱을 못한다 
import requests 
import pandas as pd 
import json  # json 형태의 문자열 데이터를 list와 dict 구조로 바꿔준다 

#Ajax 기술 - 앞으로 웹사이트가 이걸로 다 바뀐다. 
#Ajax 가져오기, 셀레니움을 사용하는 방법 
#https://sports.daum.net/record/epl
url = "https://sports.daum.net/prx/hermes/api/team/rank.json?leagueCode=epl&seasonKey=20222023&page=1&pageSize=100"
response = requests.get(url)
#print(response.status_code)
#print( response.content )
data = json.loads( response.content )
dataList = data["list"]
df = pd.DataFrame()
for item in dataList:
    newItem = dict()
    newItem["name"]= item["name"]
    newItem["win"]=item["rank"]["win"]
    newItem["draw"]=item["rank"]["draw"]
    
    df = df.append(newItem, ignore_index=True)
        
df.to_csv("해외축구.csv", encoding="utf-8", index=False)

