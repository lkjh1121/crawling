from bs4 import BeautifulSoup

f = open("test2.html", "r", encoding="utf-8")
content = f.read() #파일을 통으로 읽는다 

bs = BeautifulSoup(content, "html.parser")

table = bs.find("table", {"id":"table1"})
trList = table.find_all("tr")
for tr in trList:
    tdList = tr.find_all("td")
    for td in tdList:
        print( td.text, end="\t")
    print()
