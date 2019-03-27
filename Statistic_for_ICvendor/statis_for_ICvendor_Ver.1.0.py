# !usr/bin/python3
# -*- coding: UTF-8 -*-
# Rey
# Version: 1

import numpy as np
import pandas as pd
import os, sys, time, csv, math
from progressbar import *

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

#--- for progressbar ---#
def dosomework():
    time.sleep(0.01)
#--- to align and build data ---#
def make_df(fp, ceiling, ground):
    with open(fp, "r") as f:
        rows = f.readlines()
        df = []
        df = (rows[ceiling - 1:ground])
        df = [x.split() for x in df]
        df = pd.DataFrame(df)
        df = df[0].str.split(",", expand = True)
        df = pd.DataFrame(df.loc[:, 1:51])
        for i in range(df.shape[1]):
                df[i+1] = pd.to_numeric(df[i+1])
    return df
#--- to test the shape of Cm and hCm ---#
def pre_test_df(df):
        if df.shape[0] != 38 and df.shape[1] != 51:
            switch = False
            print(f"{filename}'s shape is wrong! {df.shape[0], df.shape[1]}")
            err_list.append(f"{filename}'s shape is wrong! {df.shape[0], df.shape[1]}")
        elif min(df.min()) < 16384:
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
def mean_(list):
    return round(sum(list) / len(list), 2)
#--- standard deviation ---#
def std_(list):
    return round(math.sqrt(sum((list - mean_(list)) ** 2) / (len(list)-1)), 3)
#--- transform list to df and reshape to (38, 51) ---#
def list_to_pd(list):
    columns_ = ["Y" + str(x) for x in range(51)]
    index_ = ["X" + str(x) for x in range(38)]
    list = np.asarray(list)
    list = list.reshape(Cm_df.shape)
    list = pd.DataFrame(list, index = index_, columns = columns_)
    return list
#--- seperate line ---#
def title(str):
    return pd.DataFrame(np.array(["Distribution"]), columns=[" "], index=[str])
# Cm_ceiling = input("Please enter the first row of full-charge Cm: ")
Cm_ceiling = 66
Cm_ceiling = int(Cm_ceiling)
Cm_ground = Cm_ceiling + 37
# hCmUpper = input("Please enter the first row of half-charge Cm: ")
hCm_ceiling = 116
hCm_ceiling = int(hCm_ceiling)
hCm_ground = hCm_ceiling + 37

good_filename = []
err_list = []
Cm_stack = np.zeros(shape=(38,51))
hCm_stack = np.zeros(shape=(38,51))

file_path = "./Python/log/"
Statistics_data_path = "./Python/Statistics_data.csv"
err_data_path = "./Python/error.csv"
files = os.listdir(file_path)

file_switch = True
try:
    title("Cm").to_csv(Statistics_data_path)
    title("error").to_csv(err_data_path)
except:
    print("Please close Statistics_data/error .csv!")
    file_switch = False

widgets = ['Progress: ',Percentage(), ' ', Bar('#'),' ', Timer(),
        ' ', ETA(), ' ', FileTransferSpeed()]
pbar = ProgressBar(widgets=widgets, maxval=10*len(files)).start()


switch = False
cnt = 0
bar = 0
if file_switch == True:
    for filename in files:
        bar += 1
        file = os.path.join(file_path, filename)
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

#===============================================================================#
            #--- to explain the method by plotting 3D model ---#
            data = np.asarray(Cm_df).flatten()
            xline = np.linspace(1, 38, 38)
            yline = np.linspace(1, 51, 51)
            x_line = []
            y_line = []
            for i in range(51):
                x_line = np.append(x_line, xline)
            for i in range(38):
                y_line = np.append(y_line, yline)

            # print(f"len(data), len(x_line), len(y_line){len(data), len(x_line), len(y_line)}")
            total_data = np.c_[x_line, y_line, data]

            # print(f"total_data shape: {total_data.shape}")

            # plot points surface
            fig = plt.figure()
            ax = fig.gca(projection='3d')
            # ax.plot_surface(total_data[:,0], total_data[:,1], total_data[:,2], rstride=1, cstride=1, alpha=0.2)
            ax.scatter(total_data[:,0], total_data[:,1], total_data[:,2]/mean_(total_data[:,2]) + cnt, c='r', s=1)
            plt.xlabel('X')
            plt.ylabel('Y')
            ax.set_zlabel('Nor.')
            ax.axis('equal')
            ax.axis('tight')
        
#===============================================================================#

        pbar.update(10 * bar)
        dosomework()
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

    Cm_mean_stack_df = list_to_pd(Cm_mean_stack)
    Cm_std_stack_df = list_to_pd(Cm_std_stack)

    print(Cm_mean_stack_df.head(), "\n", Cm_mean_stack_df.shape, "\n")
    print(Cm_std_stack_df.head(), "\n", Cm_std_stack_df.shape, "\n")


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

    hCm_mean_stack_df = list_to_pd(hCm_mean_stack)
    hCm_std_stack_df = list_to_pd(hCm_std_stack)

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
# plt.show()