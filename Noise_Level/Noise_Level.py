#!usr/bin/python3
# for analyse noise level - Stylus

import numpy as np
import pandas as pd
import os, sys

path = r"./Noise_Level/log/"
files = os.listdir(path)
for file_name in files:
	dfile_path = os.path.join(path, file_name)
	data = pd.read_csv(dfile_path)
	df = pd.DataFrame(data)
	print(df.iloc[0, 1:].min(), '\n', df.shape)