from curses import ACS_DIAMOND
from urllib import response
from bs4 import BeautifulSoup
# Ajax 기술로 코딩이 되서 데이터를 json 형태로 가져온다.
# BeautifulSoup 는 json 파싱 못한다.
import requests
import pandas as pd
import json # json 형태의 문자열 데이터를 list와 dict 구조로 바꿔준다.

# Ajax 기술 = 앞으로 웹 사이트가 대부분 다 바뀔 예정이다.
# Ajax 가져오기, 셀레니움을 사용하는 방법
# https://sports.daum.net/record/epl
url = "https://sports.daum.net/record/epl"
response = requests.get(url)
# print(response.status_code)
print(response.content)
data = json.loads(response.content )