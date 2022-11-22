"""
내 키 값: dbe6dd07fa3233cc5bc7fb8acc36351f
"""
import requests 
import json
from urllib.parse import quote
from datetime import datetime
import os
import shutil # 파일이 있는 폴더는 함부로 삭제가 안된다. 파일이 있는 폴더 삭제 시 필요

pathName = "image" # 상대경로 삭제도 된다.
# r" " rstring은 절대경로 \ 에 쓰는..
url ="https://dapi.kakao.com/v2/search/image"
custom_header = {
    "Authorization":"KakaoAK dbe6dd07fa3233cc5bc7fb8acc36351f",
}


def downloadImage(pathName,imageUrl):
    # 파일은 2가지 방식으로 저장 가능하다. : 텍스트, 바이너리
    # 텍스트 파일 : 메모장으로 읽는 게 가능
    # 바이너리 파일 : 동영상, 이미지, exe, com 파일 등 컴퓨터 메모리의 내용을 가공하지 않고 그대로 넣는다. 
    # wb  - binary로 저장
    now = datetime.now()

    # 파일 명 생성... 현재년도, 월, 일, 시간, 분, 초 + 밀리세컨드
    filename = now.strftime('%Y%m%d%H%M%S') + str(now.microsecond)
    try:
        img_res = requests.get(imageUrl)
        if img_res.status_code !=200:
            return
        f = open(f"./{pathName}/{filename}.jpg","wb")
        f.write(img_res.content) # 이미지를 binary 모드로 저장한다
        f.close()
    except:
        print(f"{imageUrl} error")
   

def initPath(pathName):
    if os.path.exists(pathName): # 기존의 폴더가 존재하면
        shutil.rmtree(pathName) # 폴더를 삭제, 안에 파일이 있으면 os로 못하므로 shutil 
    os.makedirs(pathName) # 디렉토리를 새로 만든다

def start(query="고양이",pathName="고양이",pageCnt=5): # 기본값을 주다 안주면 오류남
    pathName = query
    for page in range(1,pageCnt+1):
        params = {"query":query, "page":page, "size":50}

        print(f'--------------{page}--------------')
        response = requests.get(url, headers=custom_header,params=params)
        print(response.status_code)
        # print(response.content)
        content = json.loads(response.content)
        # meta = content["meta"]
        # print(meta["total_count"])
        # print(meta["pageable_count"])
        # print(meta["is_end"])
        documents = content["documents"] 
        for doc in documents:
            print(doc['image_url'])
            downloadImage(pathName,doc['image_url']) # 저장될 폴더명, 저장될 이미지 url

if __name__ == "__main__":
    query = input("검색어 : ")
    pathName = input("폴더명 : ")
    initPath(query)
    start(query)