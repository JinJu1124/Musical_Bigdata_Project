import pandas as pd
import os
from pandas.core.frame import DataFrame

file_list = os.listdir('Raw_Data/review_data')

file_name = [] #의미 없음(여기코드에서는)

frames = [] #데이터프레임 합치기 위한 바구니

for file in file_list:
    # 리뷰 CSV 파일들 차례로 불러오기
    df = pd.read_csv(r"Raw_Data/review_data/"+file) 
    
    df = df.drop(['Unnamed: 0'], axis=1) #숫자 열 없애주기
    musical_id = []
    text = []

    for i in df['Review Text']:
        try:
            i = i.replace('\r','')
            text.append(i)
        except:
            if i == None:
                text.append("NA")
            else:
                text.append(i)
            continue


    #확장명 없애기
    if file.count(".")==1:
        m_id = file.split('.')[0]
        file_name.append(m_id)
    else:
        for k in range(len(file)-1,0,-1):
            if file[k]=='.':
                file_name.append(file[:k])
                break
    
    #musical_id 추가하기
    for c in df['Title']:
        musical_id.append(m_id)
    
    try:
        df.drop_duplicates() #중복 없애기
        df = df.drop(['Review Text'], axis=1)
        df = df.drop(['Title'], axis=1)
        df.insert(0, "Review_Text", text)
        df.insert(0, "Musical_id", musical_id) #id추가
        frames.append(df)
        
    except:
        #빈 파일일 경우 그냥 넘어가기
        print("존재하지 않음")
        continue

dataframe = pd.concat(frames)
dataframe.rename(columns={'Review Title':'Review_title', 'Rating Star':'Rating_star', 
            'Review Id':'Review_id', 'Post Date':'Post_date'})
dataframe.to_csv('Clean_Data/clean_review_data.csv', index=False, encoding="utf-8-sig")
