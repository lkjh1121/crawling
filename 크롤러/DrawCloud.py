#헌법 파일 읽어오기 
from random import random
from konlpy.tag import Okt 
import pandas as pd 
import nltk 

def make_tokens(text, stop_words):
    okt = Okt() 
    n = okt.nouns(text) #헌법에서 명사 추출 
 
    #단어는 2글자 이상 필요없는 단어는 제거를 하자 
    tokens = [word for word in n 
                if word not in stop_words 
                and len(word)>=2]
    print ( pd.Series(tokens).unique())

    #빈도표 만들기 
    import nltk  #자연어 분석 모듈
    tokens_count = nltk.Text(tokens, name="헌법")

    #자주 사용하는 단어만 100개 추출
    data = tokens_count.vocab().most_common(100)  
    print( data )

    temp_data = dict(data) #dict타입으로 전환하기 
    return temp_data



from wordcloud import WordCloud
from PIL import Image  #이미지파일을 -> numpy 배열로 변경
from wordcloud import ImageColorGenerator 
#차트에 색을 바꿀때 필요한 라이브러리 
import numpy as np 

def make_wordcloud(temp_data, mask_image="cloud.png"):
     
    #모양 만들려고 
    mask = np.array( Image.open("./images/"+ mask_image) ) 
    #generate("파일명")
    wordcloud = WordCloud(
        font_path="./fonts/NanumGothic.ttf",
        mask = mask  
    )
    wordcloud.generate_from_frequencies(temp_data)

    #색에 대한 정보를 바꿔야 한다 
    wordcloud.recolor(color_func=multi_color_func, 
            random_state=3)
    import matplotlib.pyplot as plt 
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show() 

def multi_color_func(word, font_size, 
            position, orientation,
            random_state=None, **kwars):
    r = np.random.randint(low=100, high=255)
    g = np.random.randint(low=100, high=255)
    b = np.random.randint(low=0, high=100)
    
    return "rgb({}, {}, {})".format(r,g,b)
    #rgb(200, 190, 120)





def main(filename="카카오.txt", stop_words=[], mask_image="cloud.png"):
    f = open(filename, "r", encoding="utf-8")
    tokens = make_tokens(f.read(), stop_words)
    f.close() 

    make_wordcloud( tokens, mask_image )

if __name__ == "__main__":
    stop_words=[]
    main("할로윈.txt",stop_words,"alice_mask.png") 



