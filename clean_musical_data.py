import pandas as pd
from urllib.parse import urlparse

df = pd.read_csv(r"Raw_Data/musical_data/musical_data.csv")

#필요없는 앞에 숫자열 삭제하기
df = df.drop(['Unnamed: 0'], axis=1)


#뮤지컬인 장르만 남기기
x = df[df['Genre']!='뮤지컬'].index
df = df.drop(x)

#뮤지컬 아이디 생성
musical_id = []
for i in df['URL']:
    parts = urlparse(i)
    musicalId = parts.query
    musical_id.append(musicalId)
   


#관람연령대 
new_Age= []
#유아수준
baby = ['6세이상','12개월이상 관람가능', '20개월이상 관람가능', 
'24개월이상 관람가능', '36개월이상 관람가능', '48개월이상 관람가능', '만 5세이상', '만 6세이상', '전체관람가']

#초등학생수준
kids = ['만 7세이상','만 8세이상','8세이상 관람가능','만 9세이상', '만 10세이상', '만 11세이상', '만 12세이상',
'초등학생이상 관람가', '미취학아동입장불가']

#중학생수준
middle = ['만 13세이상', '만 14세이상', '14세 이상 관람가', '15세이상', '중학생이상 관람가']

#고등학생수준
high = ['만 15세이상', '만 16세이상','만 17세이상', '18세이상','고등학생이상 관람가']

#성인 수준
adult = ['만 18세이상','만 19세이상']
for a in df['Age']:
    if a in baby:
        new_Age.append("유아 뮤지컬")
    elif a in kids:
        new_Age.append("초등학생이상 뮤지컬")
    elif a in middle:
        new_Age.append("중학생이상 뮤지컬")
    elif a in high:
        new_Age.append("고등학생이상 뮤지컬")
    elif a in adult:
        new_Age.append("성인이상 뮤지컬")            
    else:
        new_Age.append("확인필요")

# #년도 정리하기
Periods = []
for n in df['Period']:
    period = int(n[0:4])
    Periods.append(period)
    

#태그 정리하기
tag_sale = []

onSale = ['판매중', '판매중단독판매', '판매중단독판매TOPING 할인', '판매중단독판매TOPING회원할인 10%', '판매중단독판매TOPING회원할인 32000원', 
'판매중좌석우위', '판매중좌석우위TOPING 할인', '판매중TOPING회원할인 10%', '판매중TOPING회원할인 10000원', '판매중TOPING회원할인 20%', '판매중TOPING회원할인 30%']
offSale = ['판매종료','판매종료단독판매','판매종료좌석우위']
yetSale = ['판매예정']

for t in df['Tag']:
    if t in onSale:
        tag_sale.append("판매중")
    elif t in offSale:
        tag_sale.append("판매종료")
    elif t in yetSale:
        tag_sale.append("판매예정")
    else:
        tag_sale.append("확인필요")

#필요없는 열 없애기
df = df.drop(['Age'], axis=1)
df = df.drop(['URL'], axis=1)
df = df.drop(['Tag'], axis=1)


df.insert(0, "Musical_id", musical_id)
df.insert(4, "Category", new_Age)
df.insert(8, "Period's", Periods)
df.insert(5, "Status", tag_sale)

df.to_csv('Clean_Data/clean_musical_data.csv', index=False, encoding="utf-8-sig")
