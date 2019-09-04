import numpy as np
import pandas as pd
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
plt.show()