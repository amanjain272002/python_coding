import pandas as pd

df = pd.read_csv("fortune_data.csv")
# print(df.info())
print(df.iloc[0:4,1])