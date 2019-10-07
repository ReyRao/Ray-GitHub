
import pandas as pd
import numpy as np

path = r'./Test/W9021_33x25_Side_-12dB-201910011517.csv'

with open(path, 'r', encoding='utf-8') as file:
    content = file.readlines()
    for i in range(len(content)):
        content[i] = content[i].split(',')
        content[i] = content[i][:58]

    df = pd.DataFrame(np.array(content[11:]))
    df.iloc[:, :58] = df.iloc[:, :58].astype('int')
    print(df.iloc[:, :58].dtypes)
    print(df.iloc[:, :58].max())

