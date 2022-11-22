import requests 

#get방식으로 문서를 불러온다
response = requests.get("http://google.co.kr")
print( response.status_code ) #문서를 불러온 결과를 저장한다 
#http 프로토콜 (200-ok, 404, 500, 403 .........)

if response.status_code==200:
    print("OK")
    print( response.content )
else:
    print(response.status_code, "문서를 못 불러옴")


#http://www.pythonscraping.com/exercises/exercise1.html
#