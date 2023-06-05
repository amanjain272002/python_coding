import pandas as pd
# sr = pd.Series([1,2,3])
# sr.name = "user"
# print(sr.index)
# print(sr.name)
# print(sr.to_list())
# print(sr[2])
# print(sr[0:4])
# df = pd.DataFrame({"user":[1,23],"age":[12,23]})
# print(df)

# print(df.name)
# print(type(df["user"]))

# nba = pd.read_csv("NbaInfo.csv",usecols=["Name","Team"])
# nba1 = pd.read_csv("NbaInfo.csv",usecols=["Name"]).squeeze()
# print(type(nba1))
# print(nba1.name)
# print(nba1.get(77))
# data is taking as a list
# print(nba1[[0,5]])
nba = pd.read_csv("NbaInfo.csv")
# print(100 in nba1.index)
# print(nba.info())
# nba = nba.dropna()
# print(nba.info())
# print(nba.dropna(subset=["Salary","College"]))
# nba.dropna(subset = ["Salary","College"],inplace=True)
# print(nba)
nba.dropna(inplace=True)
# print(nba)

nba["newcoll"] = 100
# print(nba)
nba["Salary"]+=nba["Salary"]*0.1
# print(nba)
# print(type(nba["Salary"]))

# print(nba["Salary"].dtype)
# print(nba["Salary"].astype(int))
# print(nba["Salary"].dtype)
# nba["Salary"] = nba["Salary"].astype(int)
# print(nba["Salary"].dtype)
# nba["Team"].unique()
print(nba["Team"].nunique())
# print(nba.info())
nba["Team"] = nba["Team"].astype("category")
# print(nba["Team"])
# print(nba.info())

print(nba[nba["Salary"]>770000])