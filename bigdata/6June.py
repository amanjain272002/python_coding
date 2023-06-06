import pandas as pd

nba = pd.read_csv("NbaInfo.csv")

# print(nba.info())
print(nba.groupby(["Team","Position"]).first())