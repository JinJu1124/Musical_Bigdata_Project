import pandas as pd
#join하기
#뮤지컬 기본데이터와 세부데이터 합치기
musical_data_df = pd.read_csv(r"Clean_Data/clean_musical_data.csv")
musical_detailed_data_df = pd.read_csv(r"Clean_Data/clean_musical_detailed_data.csv")

dataframe = pd.merge(left = musical_data_df , right = musical_detailed_data_df, how = "inner", on = "Musical_id")
dataframe.rename(columns={'Rating Count':'Rating_count'})
dataframe.to_csv("Clean_data/Musical_data.csv", index=False, encoding="utf-8-sig")

#뮤지컬 빅데이터와 리뷰데이터 합치기
df = pd.read_csv(r"Clean_data/Musical_data.csv")
df2 = pd.read_csv(r"Clean_data/clean_review_data.csv")

dataframe2 = pd.merge(left=df, right=df2, how="outer", on="Musical_id")
dataframe2.to_csv("Clean_data/Real_Musical_data.csv", index=False, encoding="utf-8-sig")
