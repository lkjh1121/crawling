from bs4 import BeautifulSoup
print("find-------------")
html = open("./test.html", "r", encoding="utf-8") #로컬문서읽기
soup = BeautifulSoup(html, "html.parser") #파싱완료된 내용을 soup라는 변수에저장 

print("find_all-------------")
#find 함수는 첫번째꺼 하나만  find("태그")
h1 = soup.find("h1") #파랗게
print(h1)  #태그까지 출력된다. 
print (h1.text ) #태그를 제외하고 내용만 출력된다. 

#전체 가져오기 - 해당 태그를 다 갖고 온다. 무조건 list형태로 반환
#반드시 index나 for를 써서 출력해야 한다 
h1List = soup.find_all("h1")
print( h1List )
for h1 in h1List:
    print( h1.text )


#속성을 사용해서 콕 찝어오기 - 매개변수를 dict타입으로 전달 
print( "-- blueTitle--")
h1 = soup.find("h1", {"id":"blueTitle"} )
print( h1.text )

print( "-- title1 --")
h1 = soup.find("h1", {"id":"title1"} )
print( h1.text )

print( "-- redTitle --")
h1s = soup.find_all("h1", {"class":"redTitle"})
for h1 in h1s:
    print( h1.text )

print("---- coffeeList -----")
ulCoffeeList = soup.find("ul", {'id':"coffeeList"})
liList = ulCoffeeList.find_all("li")
for coffee in liList:
    print(coffee.text)

print("---- jucyList -----")
ulJucyList = soup.find("ul", {'id':"jucyList"})
liList = ulJucyList.find_all("li")
for jucy in liList:
    print(jucy.text)


