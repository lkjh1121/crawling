# 셀리니움은 크롬 개발중에 만들어진 디버깅 툴

# 이벤트를 발생시켜서 해야 할 경우
from lib2to3.pgen2 import driver
from unittest.mock import patch
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
path = "./driver/chromedriver.exe"

driver = webdriver.Chrome(path) # 크롬 드라이버파일을 로딩한다.
driver.implicitly_wait(3) # 3초만 대기
# driver가 가리키는 객체안에 모든 정보가 다 들어 있다.
driver.get("https://www.python.org") # 웹 브라우저가 뜬다.
# 구글 파일을 불러와서 내부에서 처리가 다 이루어짐

# 검색 창에 검색어를 입력해서 실행시킨다.

# find_element (By.종류, "input") - 첫번째것만
# find_elements                   - 복수, 인덱스가 있어야한다
driver.implicitly_wait(1)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("pycon") # 검색창에 글씨 출력

# search_box.submit() # 서버로 현재 입력한 내용을 전송하라
search_box.send_keys(Keys.RETURN)

#content > div > section > form > ul > li:nth-child(1) > h3 > a
#content > div > section > form > ul > li:nth-child(2) > h3 > a

element = driver.find_element(By.CSS_SELECTOR, "#content > div > section > form > ul > li:nth-child(1) > h3 > a")
element.click()

print(driver.page_source)
bs = BeautifulSoup(driver.page_source, "html.parser")
h1 = bs.find("h1", {"class":"page-title"})
print(h1.text)

