from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlparse


df = pd.read_csv(r"Raw_data/musical_data/musical_detailed_data.csv")  # CSV 파일 불러오기
urls = df['URL'].values.tolist()  # 리스트에 값


musical_id = []
mean_rating = []
cnt_rating = []

# #URL을 돌면서 평점과 리뷰개수 넣기
for url in urls:
    # chrome 드라이버 객체 실행시키기
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome("/Users/dindoo/Documents/Bigdata_Musical/chromedriver", options=options)
    driver.implicitly_wait(2)
    print(url)

    #url 열기
    driver.get(url)

    parts = urlparse(url)
    musicalId = parts.query
    cnt_rating.append(musicalId)
    

    #팝업창 관리
    try:
        driver.find_element_by_css_selector('#popup-prdGuide > div > div.popupFooter > div > a').click()
    except:
        pass

    #관람 후기로 넘어가기
    try:
        driver.find_element_by_partial_link_text("관람후기").click()
    
    #리뷰평점
        try:
            is_zero = driver.find_element_by_css_selector("#productMainBody > nav > div > div > ul > li.navItem.is-active > a > span").text
            if is_zero == "0":
                ratingMean = 0
                mean_rating.append(ratingMean)
            else:
                ratingMean = driver.find_element_by_class_name("prdStarScore").text
                ratingMean = ratingMean.replace('평점:\n','')
                ratingMean = float(ratingMean)
                mean_rating.append(ratingMean)
        except:
            ratingMean = 0
            mean_rating.append(ratingMean)

        #리뷰개수
        try:
            ratingCnt = driver.find_element_by_css_selector('#prdReview > div > div.bbsListWrap.reviewAll > div.bbsListTop > div.bbsListHead > div.leftSide > strong > span').text
            ratingCnt = int(ratingCnt)
            cnt_rating.append(ratingCnt)
        except:
            ratingCnt = 0
            cnt_rating.append(ratingCnt)
        
        
            
    except:
        print("관람후기 카테고리가 없습니다.")
        ratingMean = 0
        mean_rating.append(ratingMean)
        ratingCnt = 0
        cnt_rating.append(ratingCnt)
        continue

    print("평점:",ratingMean, "리뷰개수:", ratingCnt)
    driver.close()


df.insert(16,"Rating", mean_rating)
df.insert(16,"Rating Count", cnt_rating)
print(df)
df.to_csv('musical_detailed_data.csv')
