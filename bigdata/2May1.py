# how to create excel file using python
#  https://bit.ly/3ISdDxA
import pandas as pd

# df = pd.read_csv("pokemonData.csv")
series_data = pd.read_csv("pokemonData.csv",usecols=["Pokemon"]).squeeze()
# print(type(series_data))
# print(series_data)
# df = pd.read_csv("pokemonData.csv",usecols=["Pokemon","Type"]).squeeze()
# print(type(df))
# print(df)

# print(sorted(series_data))
# print(list(series_data))

# print(series_data[[0,2]])
# print(series_data.get(90))
# print(series_data.get(900,"hello"))
# print(series_data.get([90,100,345]))

sr = pd.read_csv("pokemonData.csv",index_col="Pokemon")
# print(sr)
# print(type(sr))


# sr1 = pd.read_csv("pokemonData.csv",index_col="Pokemon").squeeze()
# print(type(sr1))
# print(sr1["Charmander"])
# sr1["Bulbasaur"]  ="Air"
# print(sr1.head(3))

df1 = pd.read_csv("pokemonData.csv",index_col="Pokemon")
# print(type(df1))
sq = df1.copy().squeeze()

sq["Bulbasaur"]  ="Air"
# print(type(sq))
print(sq)
print(df1)