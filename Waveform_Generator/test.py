import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# x = range(len(df))
# x_mod = np.linspace(x[0], x[-1], 2*len(x)-1)
# n = 0
# for index, value in enumerate(x_mod):
#     if value % 1 !=0:
#         x_mod = np.insert(x_mod, index+n, value, axis=0)
#         n += 1

# print(x_mod)

path = r'./Sample.xlsx'
df = pd.read_excel(path, header=None,  encoding='utf-8')
# m = 0
# for i in range(len(df.columns)):
#     x = range(len(df.index)-2)
#     x_mod = np.linspace(x[0], x[-1], 2*len(x)-1)
#     n = 0
#     for index, value in enumerate(x_mod):
#         if value % 1 !=0:
#             x_mod = np.insert(x_mod, index+n, value, axis=0)
#             n += 1

#     data = np.asarray(df.iloc[2:, i])
#     # print("orginal: ", data)
#     data_mod = []
#     for i in range(len(data)-1):
#         data_mod.append(data[i])
#         data_mod.append(data[i])
#         data_mod.append(data[i+1])
#     data_mod.append(data[-1])
#     print(len(x_mod), len(data_mod))
#     print(x_mod, "\n", data_mod)


ax = []
for i in range(len(df.columns)):
    ax.append(f'ax{i}')

plt.style.use('seaborn-whitegrid')
_, ax = plt.subplots(   len(df.columns), sharex=True, sharey=True,
                        gridspec_kw={'hspace': 0}, figsize=(9, 4))
legend_prperties = {'weight':'bold'}

for i in range(len(df.columns)):
    # print(f'round {i}')
    x = range(len(df.index)-2)
    x_mod = np.linspace(x[0], x[-1], 2*len(x)-1)
    n = 0
    for index, value in enumerate(x_mod):
        if value % 1 !=0:
            x_mod = np.insert(x_mod, index+n, value, axis=0)
            n += 1

    data = np.asarray(df.iloc[2:, i])
    # print("orginal: ", data)
    data_mod = []
    for j in range(len(data)-1):
        data_mod.append(data[j])
        data_mod.append(data[j])
        data_mod.append(data[j+1])
    data_mod.append(data[-1])
    # print(x_mod)
    # print(data_mod)

    ax[i].plot( x_mod, 
                data_mod, 
                label=f'{df.iloc[0, i]}->{df.iloc[1, i]}', 
                color="green")
    ax[i].legend(loc=0, frameon=False, prop=legend_prperties)
    ax[i].set_xticks(x)
    ax[i].set_yticks([-1, 0, 1])
    ax[i].set_ylim([-1.2, 1.2])

ax[0].set_title("Visualised WF")
plt.tight_layout()
plt.show()