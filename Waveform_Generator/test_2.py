<<<<<<< HEAD
import matplotlib.pyplot as plt
import pandas as pd


path = r'./Sample.xlsx'
=======
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

path = r'./vertical.xlsx'
>>>>>>> 0b75f92f364ec0d73eabb1c9fe33c74aefb2edd6
df = pd.read_excel(path, header=None,  encoding='utf-8')

ax = []
for i in range(len(df.columns)):
    ax.append(f'ax{i}')

<<<<<<< HEAD
plt.style.use('seaborn-talk')
_, ax = plt.subplots(len(df.columns), sharex=True, sharey=True, gridspec_kw={'hspace': 0}, figsize=(9, 3))
# plt.style.use('seaborn-darkgrid')

for i in range(len(df.columns)):
    x = range(len(df.iloc[2:, i]))
    ax[i].plot(x, df.iloc[2:, i], label=f'{df.iloc[0, i]}->{df.iloc[1, i]}', color="b")
    ax[i].legend(loc=0, frameon=False)
    ax[i].set_xticks(x)

print(plt.style.available)

# plt.style.use('seaborn-darkgrid')

ax[0].set_title("Visualised WF")
=======
fig, ax = plt.subplots(len(df.columns), sharex=True, sharey=True, gridspec_kw={'hspace': 0})

for i in range(len(df.columns)):
    x = range(len(df.iloc[2:, i]))
    ax[i].plot(x, df.iloc[2:, i], label=f'{df.iloc[0, i]}->{df.iloc[1, i]}')
    ax[i].legend(loc='upper right')
    
>>>>>>> 0b75f92f364ec0d73eabb1c9fe33c74aefb2edd6
plt.tight_layout()
plt.show()