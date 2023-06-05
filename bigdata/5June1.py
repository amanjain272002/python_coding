import pandas as pd
import numpy as np
nba = pd.read_csv("NbaInfo.csv")
# nba.info()

# nba.dropna(inplace=True)
# print(nba)
# print(nba.info())
# nba["Number"] = nba["Number"].astype(int)
# nba["Age"] = nba["Age"].astype(int)
# nba["Salary"] = nba["Salary"].astype(int)
# nba["Position"] = nba["Position"].astype("category")
nba.info()

nba["Name"] = nba["Name"].fillna(0)
nba["Team"] = nba["Team"].fillna(0)
nba["Number"] = nba["Number"].fillna(0)
nba["College"] = nba["College"].fillna(0)
# nba["Salary"] = nba.replace(to_replace=np.nan,value=nba["Salary"].dtype(0))
nba.info()