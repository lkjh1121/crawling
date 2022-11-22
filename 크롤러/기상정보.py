from bs4 import BeautifulSoup
import requests 
import pandas as pd 

url = "https://www.weather.go.kr/w/obs-climate/land/city-obs.do"

response = requests.get(url)
if response.status_code!=200:
    print(f"{url}을 찾을 수 없습니다.")
    exit()

def removeScript(text):
    leftPos = text.find("'") #왼쪽(0번째위치부터)에서 ' 위치를 찾기 
    rightPos = text.find("'", leftPos+1) #그 다음에 있는 '를 찾는다 
    #print(leftPos, rightPos)
    return text[leftPos+1:rightPos] #슬라이싱 
     
bs = BeautifulSoup(response.content, "html.parser")
table = bs.find("table", {"id":"weather_table"})
tbody = table.find("tbody")
trList = tbody.find_all("tr")

df = pd.DataFrame()
for tr in trList:
    tdList =  tr.find_all("td")
    
    df = df.append ({"지역이름":tdList[0].text, 
    "현재온도":tdList[5].text,
    "습도":tdList[10].text,
    "풍향":tdList[11].text,
    "풍속":removeScript(str(tdList[12])) }, ignore_index=True)
    #print( tdList[0].text , end="\t")
    #print( tdList[5].text , end="\t")
    #print( tdList[10].text , end="\t")
    #print( tdList[11].text , end="\t")
    #print( removeScript(str(tdList[12])) )
df.to_csv("기상정보.csv", encoding="CP949", index=False)




