import numpy as np
import pandas as pd
# import matplotlib as mlt
import matplotlib.pyplot as plt

dct = {
    'Date' : ['1/1/2022','1/2/2022','1/3/2022','1/4/2022','1/5/2022','1/6/2022','1/7/2022'],
    'Flavor Rating':[0.223090399,0.635885795,0.4423229,0.389127546,0.386886872,0.877983989,0.140995326],
    'Texture Rating':[0.040219739,0.938475783,0.044154093,0.549675747,0.519439148,0.19358754,0.325110425],
    'Overall Rating' :[0.600129296,0.106263596,0.59811156,0.489353146,0.988279561,0.83282696,0.105147398]
}

df = pd.DataFrame(dct)
df.set_index('Date',inplace=True)
# print(df)
df.plot(kind='bar',title='Ice Cream Rating')
# df.plot(kind='bar')
plt.show()

# x = np.linspace(0,20,100)
# plt.plot(x,np.sin(x))
# plt.show()