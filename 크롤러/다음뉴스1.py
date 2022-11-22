from bs4 import BeautifulSoup
import requests 
url="https://v.daum.net/v/20221019104208152"
response = requests.get(url)

content = response.content
soup = BeautifulSoup(content, "html.parser") 
title = soup.find("h3", {"class":"tit_view"})
print(title.text)

inputDate = soup.find("span", {"class":"num_date"})
print( inputDate.text )

contents = soup.find("div", {"class":"article_view"})
print( contents.text )



