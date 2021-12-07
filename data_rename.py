import pandas as pd

df1 = pd.read_csv(r"Clean_Data/Musical_data.csv")
df2 = pd.read_csv(r"Clean_Data/clean_review_data.csv")

df1= df1.rename(columns={'Rating Count':'Rating_count'})
df2 = df2.rename(columns={'Review Title':'Review_title', 'Rating Star':'Rating_star', 
            'Review Id':'Review_id', 'Post Date':'Post_date'})

df1.to_csv("Clean_Data/Musical_data.csv", encoding='utf-8-sig', index=False)
df2.to_csv("Clean_Data/clean_review_data.csv", encoding='utf-8-sig', index=False)