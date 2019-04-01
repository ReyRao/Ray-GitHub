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
	for row in range(df.shape[0]-1):
		# fetch the minimum value between X0 and X1(or Y0 and Y1)
		# for Y line
		for i in range(51):
			if df.iloc[row, first_Y+i] >= df.iloc[row, second_Y+i]:
				min_list.append(df.iloc[row, second_Y+i])
			else:
				min_list.append(df.iloc[row, first_Y+i])
		
		# for X line
		for j in range(38):
			if df.iloc[row, first_X+j] >= df.iloc[row, second_X+j]:
				min_list.append(df.iloc[row, second_X+j])
			else:
				min_list.append(df.iloc[row, first_X+j])

		# fetch the maximun noise value of the whole panel
		max_list.append(max(min_list))
		min_list = []

	# caculate consecutive point
	count = 0
	for i in range(len(max_list)-1):
		if max_list[i+1] > 120 and max_list[i] > 120:
			count += 1
	print(f'{file_name[:-4]}:\nConsecutive Noise: {count}')

	# plot
	plt.figure(figsize=(14, 6))
	plt.tight_layout()
	x = np.linspace(1, df.shape[0]-1, df.shape[0]-1)

	# spec 8 * 15(15 is config value)
	plt.plot(x, [120]*len(max_list), c='r')
	plt.plot(x, max_list, linewidth=0.5)
	plt.title(file_name[:-4])
	plt.ylabel("Noise Level(a.u.)")
	plt.show()
	max_list = []