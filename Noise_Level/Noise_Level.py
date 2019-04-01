#!usr/bin/python3
# for analyse noise level - Stylus

import numpy as np
import pandas as pd
import os, sys
import matplotlib.pyplot as plt

path = r"./Noise_Level/log/"
files = os.listdir(path)
first_Y = 1
second_Y = 73
first_X = 145
second_X = 217
n_Y = first_Y + 51
m_X = first_X + 38
min_list = []
max_list = []
for file_name in files:
	dfile_path = os.path.join(path, file_name)
	data = pd.read_csv(dfile_path)
	df = pd.DataFrame(data)
	# print(df.iloc[0, first_Y:n_Y], '\n', df.iloc[0, first_Y:n_Y].shape)
	for row in range(df.shape[0]-1):
		for i in range(51):
			if df.iloc[row, first_Y+i] >= df.iloc[row, second_Y+i]:
				min_list.append(df.iloc[row, second_Y+i])
			else:
				min_list.append(df.iloc[row, first_Y+i])

		for j in range(38):
			if df.iloc[row, first_X+j] >= df.iloc[row, second_X+j]:
				min_list.append(df.iloc[row, second_X+j])
			else:
				min_list.append(df.iloc[row, first_X+j])
		max_list.append(max(min_list))
		min_list = []
	# print(max_list)
	x = np.linspace(1, df.shape[0]-1, df.shape[0]-1)
	plt.plot(x, [120]*len(max_list), c='r')
	plt.plot(x, max_list)
	plt.show()