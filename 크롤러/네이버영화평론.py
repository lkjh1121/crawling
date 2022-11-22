# # 셀리니움은 크롬 개발중에 만들어진 디버깅 툴

# # 이벤트를 발생시켜서 해야 할 경우
from lib2to3.pgen2 import driver
from msilib.schema import tables
from unittest.mock import patch
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
path = "./driver/chromedriver.exe"

driver = webdriver.Chrome(path) # 크롬 드라이버파일을 로딩한다.
driver.implicitly_wait(3) # 3초만 대기

url = "https://movie.naver.com/movie/point/af/list.naver?&page=1"
driver.get(url) # 웹 브라우저가 뜬다.
driver.implicitly_wait(1)

def showData():
    table = driver.find_element(By.CLASS_NAME, "list_netizen")
    tbody = table.find_element(By.TAG_NAME, "tbody")
    trList = tbody.find_elements(By.TAG_NAME, "tr")
    for tr in trList:
        for td in tr.find_elements(By.TAG_NAME, "td"):
            print(td.text, end="\t")
        print()


#old_content > div.paging > div > a.pg_next
import time
showData()
for i in range(1, 20):
    page = driver.find_element(By.CSS_SELECTOR, "#old_content > div.paging > div > a.pg_next")
    page.click()
    print(f"--{page}로 이동")
    time.sleep(2)
    showData()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from datetime import datetime
# import logging
# import time
# import pandas as pd
# # 로거생성
# logger = logging.getLogger('movie_logger')
# logger.setLevel(logging.INFO)

# # 로거 포맷설정
# formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# # 로그 핸들러
# log_handler = logging.FileHandler('./movie_review.log')
# log_handler.setFormatter(formatter)
# logger.addHandler(log_handler)

# path = "./driver/chromedriver.exe"
# # 가상 브라우저 실행
# browser = webdriver.Chrome(path)
# logger.info('가상 브라우저 실행...')

# rank = 1
# page = 1
# while True:
#     # 네이버 영화 랭킹 이동
#     browser.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&page=%d' % page)
#     logger.info('네이버 영화 랭킹 {}페이지 이동...'.format(page))
    

#     # 영화 제목 클릭
#     tag_a_titles = browser.find_elements(By.CSS_SELECTOR, '#old_content > table > tbody > tr > td.title > div > a')
#     logger.info('{}-{} 영화 제목 클릭... :'.format(rank, tag_a_titles[rank-1].text))

#     tag_a_titles[rank-1].click()

#     # 영화 평점 클릭
#     tag_a_tab5 = browser.find_element(By.CSS_SELECTOR, "#movieEndTabMenu > li > a[title='평점']")
#     tag_a_tab5.click()
#     logger.info('영화 평점 클릭... :')

#     # 영화 제목 수집
#     title = browser.find_element(By.CSS_SELECTOR, '#content > div.article > div.mv_info_area > div.mv_info > h3 > a').text
#     logger.info('영화 제목 수집 : %s' % title)

#     # 현재 가상 브라우저의 제어를 영화 리뷰 iframe으로 전환
#     browser.switch_to.frame('pointAfterListIframe')
#     logger.info('iframe으로 전환')

#     # 영화 리뷰 출력
#     count = 1
#     while True:
#         tag_lis = browser.find_elements(By.CSS_SELECTOR, 'body > div > div > div.score_result > ul > li')
#         for li in tag_lis:
#             score = li.find_element(By.CSS_SELECTOR, '.star_score > em').text
#             reple = li.find_element(By.CSS_SELECTOR, '.score_reple > p > span:last-child').text

#             print('{},{},{},{}'.format(count, title, reple, score))
#             logger.info('{},{}'.format(count, title))
#             count += 1

#         # 다음 페이지 버튼클릭
#         try:
#             tag_a_next = browser.find_element(By.CSS_SELECTOR, 'body > div > div > div.paging > div > a.pg_next')
#             tag_a_next.click()
#             logger.info('다음 페이지 클릭')
#         except:
#             logger.error('{} 수집완료...'.format(title))
#             break


#     # 다음 순위 영화
#     rank += 1

#     if rank > page * 50:
#         # 랭킹 페이지 다음버튼 클릭
#         page += 1

#         if page > 40:
#             # 최종 종료
#             break


# logger.info('크롤링 종료...')
