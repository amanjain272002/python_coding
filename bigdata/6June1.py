import pandas as pd
df = pd.read_csv("NbaInfo.csv")
# print(df)

# print(df[df["Position"] == "PG"])
cond1 = df["Position"]=="PG"
# print(df[cond1].count())
df.dropna(how="any",inplace=True)
# print(df.groupby("Position"))
pg = df.groupby("Position")
# print(pg.count())
# print(len(pg))
# print(pg.size())
# print(pg.first())
# print(pg.get_group("PG"))
# print(pg.max())
print(pg["Age"].max())