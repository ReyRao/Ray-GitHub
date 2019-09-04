import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

path = r'./vertical.xlsx'
df = pd.read_excel(path, header=None,  encoding='utf-8')

ax = []
for i in range(len(df.columns)):
    ax.append(f'ax{i}')

fig, ax = plt.subplots(len(df.columns), sharex=True, sharey=True, gridspec_kw={'hspace': 0})

for i in range(len(df.columns)):
    x = range(len(df.iloc[2:, i]))
    ax[i].plot(x, df.iloc[2:, i], label=f'{df.iloc[0, i]}->{df.iloc[1, i]}')
    ax[i].legend(loc='upper right')
    
plt.tight_layout()
plt.show()