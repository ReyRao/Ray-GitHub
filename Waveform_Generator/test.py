import numpy as np
import pandas as pd
<<<<<<< HEAD
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
=======
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="darkgrid", rc={"axes.facecolor": (0, 0, 0, 0)})

# Create the data
# rs = np.random.RandomState(1979)
# x = rs.randn(2)
# g = np.tile(list("AB"), 1)
# df = pd.DataFrame(dict(x=x, g=g))
# m = df.g.map(ord)
# df["x"] += m

path = r'./vertical.xlsx'
df = pd.read_excel(path, encoding='utf-8')

print(df)

# Initialize the FacetGrid object
# pal = sns.cubehelix_palette(10, rot=-.65, light=.8)

g = sns.FacetGrid(df, row='G1', aspect=10, height=1)
# Draw the densities in a few steps
# g.map(sns.lineplot, "G1", shade=True, lw=1.5, bw=.2)
# g.map(sns.lineplot, "G1", color="w", lw=2, bw=.2)
g.map(plt.plot, "G1")

# Define and use a simple function to label the plot in axes coordinates
# def label(x, color, label):
#     ax = plt.gca()
#     ax.text(0, .2, label, fontweight="bold", color=color,
#             ha="left", va="center", transform=ax.transAxes)

# g.map(label, "G1")

# Set the subplots to overlap
g.fig.subplots_adjust(hspace=-.25)

# Remove axes details that don't play well with overlap
g.set_titles("")
g.set(yticks=[])
g.despine(bottom=True, left=True)
>>>>>>> 0b75f92f364ec0d73eabb1c9fe33c74aefb2edd6
plt.show()