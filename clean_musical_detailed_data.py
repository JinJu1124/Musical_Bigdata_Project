import pandas as pd
from urllib.parse import urlparse

df = pd.read_csv(r"Raw_Data/musical_data/musical_detailed_data.csv")

#필요없는 앞에 숫자열 삭제하기
df = df.drop(['Unnamed: 0'], axis=1)
df = df.drop(['Unnamed: 0.1'], axis=1)

#뮤지컬 아이디 생성
musical_id = []
for i in df['URL']:
    parts = urlparse(i)
    musicalId = parts.query
    musical_id.append(musicalId)

#취소공연
cancel_status = []
for c in df['Status']:
    if c == "판매취소":
        cancel_status.append("판매취소")
    else:
        cancel_status.append("관련없음")     

#성별 별 예매율
man_ticket = []
woman_ticket = []

like_man = df['Like_man'].values.tolist()
like_woman = df['Like_woman'].values.tolist()

for man in like_man:
    try:
        man = man.replace('%', '')
        man = float(man)
        man_ticket.append(man)
    except:
        man_ticket.append("NA")

for woman in like_woman:
    try:
        woman = woman.replace('%', '')
        woman = float(woman)
        woman_ticket.append(woman)
    except:
        woman_ticket.append("NA")

#예매율
who = []
woman_ = 0
for man_ in man_ticket :
    if man_ < woman_ticket[woman_]:
        who.append("woman")
    elif man_ > woman_ticket[woman_]:
        who.append("man")
    else:
        who.append("NA")
    woman_ = woman_ + 1


# 연령별 예매율
ten_like = []
twenty_like = []
thirty_like = []
fourty_like = []
fifty_like = []

ten = df['Like_age_10'].values.tolist()
twenty = df['Like_age_20'].values.tolist()
thirty = df['Like_age_30'].values.tolist()
fourty = df['Like_age_40'].values.tolist()
fifty= df['Like_age_50'].values.tolist()

#float으로 만들어주기
for age in ten:
    try:
        age = age.replace('%', '')
        age = float(age)
        ten_like.append(age)
    except:
        ten_like.append(None)

for age in twenty:
    try:
        age = age.replace('%', '')
        age = float(age)
        twenty_like.append(age)
    except:
        twenty_like.append(None)

for age in thirty:
    try:
        age = age.replace('%', '')
        age = float(age)
        thirty_like.append(age)
    except:
        thirty_like.append(None)

for age in fourty:
    try:
        age = age.replace('%', '')
        age = float(age)
        fourty_like.append(age)
    except:
        fourty_like.append(None)

for age in fifty:
    try:
        age = age.replace('%', '')
        age = float(age)
        fifty_like.append(age)
    except:
        fifty_like.append(None)

#가장 예매율 높은 연령 찾기
age_best = []
dataframe = pd.DataFrame({'10대' : ten_like, '20대' : twenty_like, '30대' : thirty_like, '40대' : fourty_like, '50대':fifty_like})
maxs = dataframe.idxmax(axis=1, skipna=True).values.tolist()

for u in maxs:
    age_best.append(u)

#필요없는 열 없애기
df = df.drop(['Title'], axis=1)
df = df.drop(['Genre'], axis=1)
df = df.drop(['Place'], axis=1)
df = df.drop(['Time'], axis=1)
df = df.drop(['Period'], axis=1)
df = df.drop(['Age'], axis=1)
df = df.drop(['URL'], axis=1)
df = df.drop(['Like_man'], axis=1)
df = df.drop(['Like_woman'], axis=1)
df = df.drop(['Like_age_10'], axis=1)
df = df.drop(['Like_age_20'], axis=1)
df = df.drop(['Like_age_30'], axis=1)
df = df.drop(['Like_age_40'], axis=1)
df = df.drop(['Like_age_50'], axis=1)
df = df.drop(['Status'], axis=1)


#필요한열 추가하기
df.insert(0 , "Cancel_status", cancel_status)
df.insert(0, "Best_age", age_best)
df.insert(0, 'Ticket_age_50(%)', fifty_like)
df.insert(0, 'Ticket_age_40(%)', fourty_like)
df.insert(0, 'Ticket_age_30(%)', thirty_like)
df.insert(0, 'Ticket_age_20(%)', twenty_like)
df.insert(0, 'Ticket_age_10(%)', ten_like)
df.insert(0 , "Best_gender", who)
df.insert(0, 'Ticket_gender_woman(%)', woman_ticket)
df.insert(0, 'Ticket_gender_man(%)', man_ticket)
df.insert(0, "Musical_id", musical_id)

df.to_csv('Clean_Data/clean_musical_detailed_data.csv', index=False, encoding="utf-8-sig")
