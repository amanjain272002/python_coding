import pandas as pd
df = pd.read_csv("fortune_data.csv")
print(df.info())
# print(df["Rank"].nunique())
df.set_index("Rank",inplace=True)
# print(df[df["Rank"].duplicated()])
# print(df.info())
# print(df)

# df.drop_index(subset="Rank", inplace=True)
# print(df)
df.reset_index(drop=True,inplace=True)
print(df.info())