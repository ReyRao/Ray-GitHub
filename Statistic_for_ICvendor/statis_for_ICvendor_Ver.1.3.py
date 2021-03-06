# !usr/bin/python3
# to compatable with both 103 and 133
#
# Rey
# Version: 1.3
##############################################################################

import numpy as np
import pandas as pd
import os
import sys
import time
import csv
import math
import progressbar
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


#--- to align and build data ---#
def make_df(fp, ceiling, ground):
    with open(fp, "r") as f:
        rows = f.readlines()
        df = []
        df = (rows[ceiling - 1:ground])
        df = [x.split() for x in df]
        df = pd.DataFrame(df)
        df = df[0].str.split(",", expand = True)
        if sony103 == True:
            df = pd.DataFrame(df.loc[:, 1:51])
        else:
            df = pd.DataFrame(df.loc[:, 1:67])
        for i in range(df.shape[1]):
            df[i+1] = pd.to_numeric(df[i+1])
    return df


#--- to test the shape of Cm and hCm ---#
def pre_test_df(df):
        if df.shape[0] != 38 and df.shape[0] != 41: 
            if df.shape[1] != 51 and df.shape[1] != 67:
                switch = False
                print(f"{filename}'s shape is wrong! {df.shape[0], df.shape[1]}")
                err_list.append(
                    f"{filename}'s shape is wrong! {df.shape[0], df.shape[1]}")
        if min(df.min()) < 16384:
            switch = False
            print(f"{filename} have to be confirmed again!")
            err_list.append(f"{filename} have to be confirmed again!")
        else:
            switch = True
        return switch


#--- row's from 0 to 37, total 38 rows ---#
def z_row(df, stack, row):
    row_stack = []
    num = stack.shape[0]//df.shape[0]
    for j in range(df.shape[1]):
        row_stack.append([])
        for i in range(1, num):
            row_stack[j].append(stack[row + df.shape[0]*i, j])
    return row_stack


#--- average value ---#
def mean_(_list):
    return round(sum(_list) / len(_list), 2)


#--- standard deviation ---#
def std_(_list):
    return round(
            math.sqrt(sum((_list - mean_(_list)) ** 2) / (len(_list)-1)), 3)


#--- transform list to df and reshape to (38, 51) ---#
def list_to_pd(_list, df):
    columns_ = ["Y" + str(x) for x in range(df.shape[1])]
    index_ = ["X" + str(x) for x in range(df.shape[0])]
    _list = np.asarray(_list)
    _list = _list.reshape(Cm_df.shape)
    _list = pd.DataFrame(_list, index = index_, columns = columns_)
    return _list


#--- seperate line ---#
def title(_str):
    return pd.DataFrame(
            np.array(["Distribution"]),
            columns=[" "], index=[_str])


#--- to catch the row No. ---#
def rowNumber(path):
    CmUpper = 0
    hCmUpper = 0
    CmBottom = 0
    hCmBottom = 0
    fp = os.path.join(path, filename)
    with open(fp, "r") as f:
        iter_f = iter(f)
        #Find the index of differential
        for i, line in enumerate(iter_f):
            if "Reference Value at Charger Time" in line:
                CmUpper = i + 3
            if "Half CT value. CT=" in line:
                CmBottom = i - 10
                hCmUpper = i + 3
                if sony103 == True:
                    hCmBottom = i + 40
                else:
                    hCmBottom = i + 43
    return CmUpper, CmBottom, hCmUpper, hCmBottom


global sony103
sony103 = False
sony = input("Are they 10.3 inch panel: (Y/N)")
if sony == 'Y' or sony == 'y':
    sony103 = True
else:
    sony103 = False

good_filename = []
err_list = []

file_path = './log'
Statistics_data_path = "./Statistics_data.csv"
err_data_path = "./error.csv"
files = os.listdir(file_path)

file_switch = True
try:
    title("Cm").to_csv(Statistics_data_path)
    title("error").to_csv(err_data_path)
except:
    print("Please close Statistics_data/error .csv!")
    file_switch = False

if sony103 == True:
    Cm_stack = np.zeros(shape=(38, 51))
    hCm_stack = np.zeros(shape=(38, 51))
else:
    Cm_stack = np.zeros(shape=(41, 67))
    hCm_stack = np.zeros(shape=(41, 67))


widgets = ['Progress: ', progressbar.Percentage(),
            ' ', progressbar.Bar('#'),' ', progressbar.Timer(),
            ' ', progressbar.ETA(),
            ' ', progressbar.FileTransferSpeed()]
pbar = progressbar.ProgressBar(widgets=widgets, maxval=10*len(files)).start()


switch = False
cnt = 0
bar = 0
if file_switch == True:
    for filename in files:
        bar += 1
        file = os.path.join(file_path, filename)

        try:
            Cm_ceiling, Cm_ground, hCm_ceiling, hCm_ground = rowNumber(file_path)
        except:
            print(f"{file} rows's range wrong!")

        try:
            Cm_df = make_df(file, Cm_ceiling, Cm_ground)
        except:
            print(f"{filename} Full-charged Cm cannot be arranged!")
            err_list.append(f"{filename} Full-charged Cm cannot be arranged!")
            switch = False

        try:
            hCm_df = make_df(file, hCm_ceiling, hCm_ground)

        except:
            print(f"{filename} Half-charged Cm cannot be arranged!")
            err_list.append(f"{filename} Half-charged Cm cannot be arranged!")
            switch = False

        try:
            switch = pre_test_df(Cm_df)
            if switch == True:
                switch = pre_test_df(hCm_df)
        except ValueError:
            print(f"{filename} min() arg is an empty sequence")
            err_list.append(f"{filename} min() arg is an empty sequence")
            switch = False

        if switch == True:
            good_filename.append(filename)
            cnt += 1
            Cm_array = np.asarray(Cm_df)
            hCm_array = np.asarray(hCm_df)
            Cm_stack = np.vstack((Cm_stack, Cm_array))
            hCm_stack = np.vstack((hCm_stack, hCm_array))

        pbar.update(10 * bar)
        time.sleep(0.1)
    pbar.finish()

    #--- Cm ---#
    Cm_row_stack = []
    for i in range(Cm_df.shape[0]):
        Cm_row_stack.append([])
        Cm_row_stack[i] = z_row(Cm_df, Cm_stack, i)

    Cm_row_stack = np.asarray(Cm_row_stack)
    Cm_mean_stack = []
    Cm_std_stack = []
    for i in range(Cm_df.shape[0]):
        for j in range(Cm_df.shape[1]):
            Cm_mean_stack.append(mean_(Cm_row_stack[i, j]))
            Cm_std_stack.append(std_(Cm_row_stack[i, j]))

    Cm_mean_stack_df = list_to_pd(Cm_mean_stack, Cm_df)
    Cm_std_stack_df = list_to_pd(Cm_std_stack, Cm_df)

    # print(Cm_mean_stack_df.head(), "\n", Cm_mean_stack_df.shape, "\n")
    # print(Cm_std_stack_df.head(), "\n", Cm_std_stack_df.shape, "\n")


    #--- hCm ---#
    hCm_row_stack = []
    for i in range(hCm_df.shape[0]):
        hCm_row_stack.append([])
        hCm_row_stack[i] = z_row(hCm_df, hCm_stack, i)

    hCm_row_stack = np.asarray(hCm_row_stack)
    hCm_mean_stack = []
    hCm_std_stack = []
    for i in range(hCm_df.shape[0]):
        for j in range(hCm_df.shape[1]):
            hCm_mean_stack.append(mean_(hCm_row_stack[i, j]))
            hCm_std_stack.append(std_(hCm_row_stack[i, j]))

    hCm_mean_stack_df = list_to_pd(hCm_mean_stack, hCm_df)
    hCm_std_stack_df = list_to_pd(hCm_std_stack, hCm_df)

    # print(hCm_mean_stack_df, "\n", hCm_mean_stack_df.shape, "\n")
    # print(hCm_std_stack_df, "\n", hCm_std_stack_df.shape, "\n")

#--- save data ---#
    title("Cm").to_csv(Statistics_data_path)
    Cm_mean_stack_df.to_csv(Statistics_data_path, mode="a")

    title("half_Cm").to_csv(Statistics_data_path, mode="a")
    hCm_mean_stack_df.to_csv(Statistics_data_path, mode="a")

    title("Cm_STD").to_csv(Statistics_data_path, mode="a")
    Cm_std_stack_df.to_csv(Statistics_data_path, mode="a")

    title("half_Cm_STD").to_csv(Statistics_data_path, mode="a")
    hCm_std_stack_df.to_csv(Statistics_data_path, mode="a")
    
    err_df = pd.DataFrame(err_list, columns=["error discription:"])
    err_df.to_csv(err_data_path)

#===============================================================================#
#--- to explain the method by plotting Cm_stack_data 3D model ---#
Cm_mean_stack_data = np.asarray(Cm_mean_stack_df).flatten()
hCm_mean_stack_data = np.asarray(hCm_mean_stack_df).flatten()
Cm_std_stack_data = np.asarray(Cm_std_stack_df).flatten()
hCm_std_stack_data = np.asarray(hCm_std_stack_df).flatten()
xline = np.linspace(1, Cm_mean_stack_df.shape[0], Cm_mean_stack_df.shape[0])
yline = np.linspace(1, Cm_mean_stack_df.shape[1], Cm_mean_stack_df.shape[1])
x_line = []
y_line = []
for i in range(Cm_mean_stack_df.shape[1]):
    x_line = np.append(x_line, xline)
for i in range(Cm_mean_stack_df.shape[0]):
    y_line = np.append(y_line, yline)

# print(f"len(data), len(x_line), len(y_line){len(data), len(x_line), len(y_line)}")
Cm_mean_stack_total_data = np.c_[x_line, y_line, Cm_mean_stack_data]
hCm_mean_stack_total_data = np.c_[x_line, y_line, hCm_mean_stack_data]
Cm_std_stack_toal_data = np.c_[x_line, y_line, Cm_std_stack_data]
hCm_std_stack_toal_data = np.c_[x_line, y_line, hCm_std_stack_data]
# print(f"Cm_stack_data shape: {Cm_stack_data.shape}")

# plot points surface
fig = plt.figure(figsize=plt.figaspect(0.8))
ax = fig.add_subplot(2, 2, 1, projection='3d')
ax.scatter(Cm_mean_stack_total_data[:,0],
           Cm_mean_stack_total_data[:,1],
           Cm_mean_stack_total_data[:,2],
           c='r', s=10)
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Cm Mean")
ax.set_zlabel('Cm Mean')
ax.axis('equal')
ax.axis('tight')

ax = fig.add_subplot(2, 2, 2, projection='3d')
ax.scatter(hCm_mean_stack_total_data[:,0],
           hCm_mean_stack_total_data[:,1],
           hCm_mean_stack_total_data[:,2],
           c='y', s=10)
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Half-charge Cm Mean")
ax.set_zlabel('Half-charge Cm Mean')
ax.axis('equal')
ax.axis('tight')

ax = fig.add_subplot(2, 2, 3, projection='3d')
ax.scatter(Cm_std_stack_toal_data[:,0],
           Cm_std_stack_toal_data[:,1],
           Cm_std_stack_toal_data[:,2],
           c='b', s=10)
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Cm Standard Deviation")
ax.set_zlabel('Cm STD')
ax.axis('equal')
ax.axis('tight')

ax = fig.add_subplot(2, 2, 4, projection='3d')
ax.scatter(hCm_std_stack_toal_data[:,0],
           hCm_std_stack_toal_data[:,1],
           hCm_std_stack_toal_data[:,2],
           c='g', s=10)
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Half-charge Cm Standard Deviation")
ax.set_zlabel('Half-charge Cm STD')
ax.axis('equal')
ax.axis('tight')

#===============================================================================#

plt.show()