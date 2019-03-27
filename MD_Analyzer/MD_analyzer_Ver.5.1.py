# !usr/bin/Python3
# -*- coding: UTF-8 -*-
# to analyze Solomon's the comprehensive Cm(full charge)
# Rey
# Version: 5.1

import numpy as np
import pandas as pd
import os, sys
import csv
import time
import math
from progressbar import *
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import scipy.linalg
from mpl_toolkits.mplot3d import Axes3D

def makeDf(fp, upper, bottom):
    with open(fp, "r") as f:
        rows = f.readlines()
        df = []
        df = (rows[upper - 1:bottom])
        df = [x.split() for x in df]
        df = pd.DataFrame(df)
        df = df[0].str.split(",", expand = True)
        df = pd.DataFrame(df.loc[:, 1:51])
        for i in range(df.shape[1]):
                df[i+1] = pd.to_numeric(df[i+1])
    return df
#--- average value ---#
def mean_(list):
    return round(sum(list) / len(list), 5)

def std_(list):
    return round(math.sqrt(sum((list - mean_(list)) ** 2) / (len(list)-1)), 5)

def remove(list, obj):
    return [x for x in list if x != obj]

def index(list, value):
    return [f"Y{i}-Y{i+1}" for i, x in enumerate(list) if x == value]

def pre_test(df):
        emp_cnt = 0
        if df.shape[0] != 38 and df.shape[1] != 51:
            switch = False
            emp_cnt += 1
            print(f"{file}'s shape is wrong! {df.shape[0], df.shape[1]}")
            err_list.append(f"{file}'s shape is wrong! {df.shape[0], df.shape[1]}")
        elif min(df.min()) < 16384:
            switch = False
            print(f"{file} have to be confirmed again!(<16384)")
            err_list.append(f"{file} have to be confirmed again!(<16384)")
        else:
            switch = True
        return switch, emp_cnt

def dosomework():
    time.sleep(0.01)

def Test_1(df):
    diff = 0
    count = 0
    diff = max(df.max()) - min(df.min())
    if (diff) < 1800:
        count += 0
    elif (diff) >= 1800:
        count += 1
    return count

def Test_2(df):
    count = 0
    for j in range(df.shape[1]):
        for i in range(df.shape[0]):
            if df.iloc[i, j] >= 23500 or df.iloc[i, j] <= 20500:
                count += 1
            else:
                count += 0
    return count
# ---old method--- #
def Test_4(df):
    dfmean = round(mean_(df[0:].mean()), 2)
    ub = round(mean_(df[0:].mean()) * 0.15, 2)
    bb = round(mean_(df[0:].mean()) * 0.1, 2)
    count = 0
    for j in range(df.shape[1]):
        for i in range(df.shape[0]):
            if (df.iloc[i, j] - dfmean) >= 0:
                if (df.iloc[i, j] - dfmean) >= ub:
                    count += 1
            elif (df.iloc[i, j] - dfmean) <= 0:
                if (df.iloc[i, j] - dfmean) <= -bb:
                    count += 1
            else:
                count += 0
    return count
# ---vendor's method--- #
def Test_3(df):
    count = 0
    for i in range(len(df.columns)):
        x = np.linspace(1, len(df.index), len(df.index))
        y = np.asarray(df[i+1])
        fit = np.polyfit(x, y, 2, full=True)[0]
        formula = np.poly1d(fit)
        reg = formula(x)
        ceiling = reg * 1.15
        ground = reg * 0.9
        for j in range(len(df.index)):
            if y[j] > reg[j]:
                if y[j] >= ceiling[j]:
                    count += 1
            elif y[j] < reg[j]:
                if y[j] <= ground[j]:
                    count += 1
            else:
                count += 0
    return count

def analyze(data, order):
    x = np.linspace(1, len(data), len(data)) 
    y = data
    fit = np.polyfit(x, y, order, full=True)[0]
    formula = np.poly1d(fit)
    y_bar = mean_(data)
    y_hat = formula(x)
    SSR = sum((y_hat - y_bar)**2)
    SSE = sum((y - y_hat)**2)
    SSTO = sum((y - y_bar)**2)
    MAE = sum(abs(y - y_hat))/len(y)
    RMSE = math.sqrt(sum((y - y_hat)**2)/len(y))
    return SSR/SSTO, SSE, MAE, RMSE

def MDrow(path):
    YMD = []
    YMDline = 0
    switch = True
    fp = os.path.join(path, file)
    with open(fp, "r") as f:
        iter_f = iter(f)
        #Find the index of differential
        for i, line in enumerate(iter_f):
            if "36) MicroDefect" in line:
                YMDline = i + 16
    with open(fp, "r") as f:
        rows = f.readlines()
        YMD = rows[YMDline]
        YMD = YMD.replace("%", "")
        YMD = YMD.replace("Diff", "")
        YMD = YMD.replace(",", " ")
        YMD = [float(x) for x in YMD.split()]
    if len(YMD) == 0:
        print("Y MD is empty!")
        switch = False
    return YMD, switch

def rowNumber(path):
    CmUpper = 0
    hCmUpper = 0
    fp = os.path.join(path, file)
    with open(fp, "r") as f:
        iter_f = iter(f)
        #Find the index of differential
        for i, line in enumerate(iter_f):
            if "Reference Value at Charger Time" in line:
                CmUpper = i + 3
                hCmUpper = i + 53
    CmBottom = CmUpper + 37
    hCmBottom = hCmUpper + 37
    return CmUpper, CmBottom, hCmUpper, hCmBottom

__mode = input("Please set analyze mode!\n\
    1 for SSE\n\
    2 for R square\n\
    3 for MAE\n\
    4 for RMSE\n\
    (default = MAE)\n")
if __mode != "":
    __mode = int(__mode)
else:
    __mode = 3

rename_mode = input("Do you want to rename the data?\n\
    (y/n, default = n)\n")
rename_mode = str(rename_mode)
if rename_mode == "y":
    rename_mode = True
elif rename_mode == "n" or rename_mode == "":
    rename_mode = False

plot_all_mode = input("Do you want to plot all the results?\n\
    (y/n, default = n)\n")
plot_all_mode = str(plot_all_mode)
if plot_all_mode == "y":
    plot_all_mode = True
elif plot_all_mode == "n" or plot_all_mode == "":
    plot_all_mode = False

if plot_all_mode==True:
    true_pass = False
else:
    true_pass = input("Do you want to plot the mean and threthold values?\n\
    (y/n, default = n)\n")
    true_pass = str(true_pass)
    if true_pass == "y":
        true_pass = True
    elif true_pass == "n" or true_pass == "":
        true_pass = False

path = "./log/"
spath = "./save.csv"
err_path = "./err.csv"

files = os.listdir(path)

pre_write = {
    "test":[0]
}
predf = pd.DataFrame(pre_write)

save_mode = True

try:
    predf.to_csv(spath)
    predf.to_csv(err_path)
except PermissionError:
    print("Please close save/err.csv !")
    save_mode = False


file_list = []
CmSTDlist = []
err_list = []
Test_1_count_list = []
Test_2_count_list = []
Test_3_count_list = []
Test_4_count_list = []
log10_SSE_list = []
SSE_list = []
SSE_pass_list = []
r2_list = []
r2_pass_list = []
MAE_list = []
MAE_pass_list = []
RMSE_list = []
RMSE_pass_list = []
YMD_list = []
if save_mode==True:
    widgets = ['Progress: ',Percentage(), ' ', Bar('#'),' ', Timer(),
            ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=10*len(files)).start()

    switch = False
    good_cnt = 0
    test_fail = 0
    data_error = 0
    k = 0
    for file in files:
        
        k += 1
        fp = os.path.join(path, file)
        
        try:
            CmUpper, CmBottom, hCmUpper, hCmBottom = rowNumber(path)
            # print(CmUpper, CmBottom, hCmUpper, hCmBottom)
        except:
            print(f"{file} rows' range wrong!")
            err_list.append(f"{file} rows' range wrong!")
            switch = False

        try:
            CmTb = makeDf(fp, CmUpper, CmBottom)
            hCmTb = makeDf(fp, hCmUpper, hCmBottom)
        except:
            print(f"{file} Full-charge Cm cannot be arranged!")
            err_list.append(f"{file} Full-charge Cm cannot be arranged!")
            switch = False

        try:
            switch, _ = pre_test(CmTb)
            if switch == True:
                switch, _ = pre_test(hCmTb)

        except ValueError:
            print(f"{file} min() arg is an empty sequence")
            err_list.append(f"{file} min() arg is an empty sequence")
            switch = False
        try:
            if switch == True:
                YMD, switch = MDrow(path)
                YMD_list.append(max(YMD))
            else:
                print(f"{file} MD can't be analyzed!")
                err_list.append(f"{file} MD can't be analyzed!")
                switch = False
        except:
            print(f"{file} MD analyze fail!")
            switch = False

        if switch == True:
            file_list.append(file)
            try:
                Test_1_count = Test_1(CmTb)
                Test_1_count_list.append(Test_1_count)
            except:
                print(f"{file} test_1 cannot be analyzed!")
                err_list.append(f"{file} test_1 cannot be analyzed!")

            try:
                Test_2_count = Test_2(CmTb)
                Test_2_count_list.append(Test_2_count)
            except:
                print(f"{file} Test_2 cannot be analyzed!")
                err_list.append(f"{file} test_2 cannot be analyzed!")

            try:
                Test_3_count = Test_3(CmTb)
                Test_3_count_list.append(Test_3_count)
            except:
                print(f"{file} Test_3 cannot be analyzed")
                err_list.append(f"{file} test_3 cannot be analyzed!")

            try:
                Test_4_count = Test_4(CmTb)
                Test_4_count_list.append(Test_4_count)
            except:
                print(f"{file} Test_4 cannot be analyzed")
                err_list.append(f"{file} test_4 cannot be analyzed!")
                
            if Test_1_count+Test_2_count+Test_3_count != 0:
                test_fail += 1
                if rename_mode == True:
                    os.rename(os.path.join(path, file), os.path.join(path, "FAIL_"+file))


                analysis_mode = False
                if __mode == 1:
                    log10_SSE_list.append(-1)
                    SSE_list.append(-1)
                elif __mode == 2:
                    r2_list.append(-1)
                elif __mode == 3:
                    MAE_list.append(-1)
                elif __mode == 4:
                    RMSE_list.append(-1)

            else:
                analysis_mode = True
            
            if analysis_mode == True:
                good_cnt += 1
                x = np.linspace(1, 51, 51)
                y = np.array(CmTb.mean())
                r2, SSE, MAE, RMSE = analyze(y, 2)
                SSE_list.append(round(SSE, 3))
                SSE_pass_list.append(round(SSE, 3))
                log10_SSE_list.append(round(math.log10(SSE), 3))
                r2_list.append(round(r2, 3))
                r2_pass_list.append(round(r2, 3))
                MAE_list.append(round(MAE, 3))
                MAE_pass_list.append(round(MAE, 3))
                RMSE_list.append(round(RMSE, 3))
                RMSE_pass_list.append(round(RMSE, 3))

                if __mode == 1:
                    try:
                        if rename_mode == True:
                            os.rename(os.path.join(path, file), os.path.join(path, f"{round(SSE, 3)}_" + file))
                    except:
                        print(f"{file} SSE linear regresion error!")
                elif __mode == 2:
                    try:
                        
                        if rename_mode == True:
                            os.rename(os.path.join(path, file), os.path.join(path, f"{round(r2, 3)}_" + file))
                    except:
                        print(f"{file} R2 linear regresion error!")
                elif __mode == 3:
                    try:
                        
                        if rename_mode == True:
                            os.rename(os.path.join(path, file), os.path.join(path, f"{round(MAE, 3)}_" + file))
                    except:
                        print(f"{file} MAE linear regresion error!")
                elif __mode == 4:
                    try:
                        
                        if rename_mode == True:
                            os.rename(os.path.join(path, file), os.path.join(path, f"{round(RMSE, 3)}_" + file))
                    except:
                        print(f"{file} RMSE linear regresion error!")
                    

        else:
            data_error += 1
            if rename_mode == True:
                os.rename(os.path.join(path, file), os.path.join(path, "FAIL_"+file))

            if __mode == 1:
                log10_SSE_list.append(-1)
                SSE_list.append(-1)
            elif __mode == 2:
                r2_list.append(-1)
            elif __mode == 3:
                MAE_list.append(-1)
            elif __mode == 4:
                RMSE_list.append(-1)

            print(f"{file} is empty!")
            err_list.append(f"{file} is empty!")
            file_list.append(file)
            Test_1_count_list.append(-1)
            Test_2_count_list.append(-1)
            Test_3_count_list.append(-1)
            Test_4_count_list.append(-1)
        
        pbar.update(10 * k)
        dosomework()
    pbar.finish()


'''#--- plot regression ---#'''
if plot_all_mode == False:
    if __mode == 1:
        data = log10_SSE_list
        plt_data = SSE_list
        pass_data = SSE_pass_list
        y_label = "SSE"
    elif __mode == 2:
        data = r2_list
        plt_data = data
        pass_data = r2_pass_list
        y_label = "R square"
    elif __mode == 3:
        data = MAE_list
        plt_data = data
        pass_data = MAE_pass_list
        y_label = "MAE"
    elif __mode == 4:
        data = RMSE_list
        plt_data = data
        pass_data = RMSE_pass_list
        y_label = "RMSE"
    x = np.linspace(1, len(data), len(data))
    plt.scatter(x, plt_data)
    plt.ylabel(y_label)
    plt.xlabel("# of pieces")

else:
    if __mode == 1:
        data = log10_SSE_list
        y_label = "SSE"
    elif __mode == 2:
        data = r2_list
        y_label = "R square"
    elif __mode == 3:
        data = MAE_list
        y_label = "MAE"
    elif __mode == 4:
        data = RMSE_list
        y_label = "RMSE"
    
    SSE_plt_data = SSE_list
    r2_plt_data = r2_list
    MAE_plt_data = MAE_list
    RMSE_plt_data = RMSE_list

    fig = plt.figure()
    x = np.linspace(1, len(data), len(data))
    plt.subplot(221)
    plt.scatter(x, SSE_plt_data)
    plt.title("SSE")
    plt.ylabel("SSE")
    plt.xlabel("# of pieces")

    plt.subplot(222)
    plt.scatter(x, r2_plt_data)
    plt.title("R square")
    plt.ylabel("R square")
    plt.xlabel("# of pieces")

    plt.subplot(223)
    plt.scatter(x, MAE_plt_data)
    plt.title("MAE")
    plt.ylabel("MAE")
    plt.xlabel("# of pieces")

    plt.subplot(224)
    plt.scatter(x, RMSE_plt_data)
    plt.title("RMSE")
    plt.ylabel("RMSE")
    plt.xlabel("# of pieces")

save_dict = {
    "filename": file_list,
    "Max. - Min. < 1800": Test_1_count_list,
    "20500 < Cm < 23500": Test_2_count_list,
    "(0.9Cm_hat) < Cm < (1.15Cm_hat)": Test_3_count_list,
    "(0.9mean) < Cm < (1.15mean)": Test_4_count_list,
    "Y_Max MicroDefect": YMD_list,
    y_label: data
    }

err_dict = {
    "Error": err_list
    }

save_df = pd.DataFrame(save_dict)

err_df = pd.DataFrame(err_dict)
err_df.to_csv(err_path, index=False)

try:
    save_df.to_csv(spath, index=False)
except PermissionError:
    print("Please close the save data!")

if true_pass == True and plot_all_mode==False:
    if __mode != 2:
        #--- exclude "Fail"(-1) data already ---#
        spec_ceiling = mean_(np.asarray(pass_data)) + 3 * std_(np.asarray(pass_data))
        spec_bottom = mean_(np.asarray(pass_data)) - 3 * std_(np.asarray(pass_data))
        if __mode == 1:
            print(f"SSE threshold value: {spec_ceiling}")
            log10_spec_ceiling = math.log10(spec_ceiling)
            print(f"log10(SSE) threshold value: {log10_spec_ceiling}")
        else:
            print(f"{y_label} treshold value: {spec_ceiling}")
        plt.plot(x, [mean_(np.asarray(pass_data))] * len(x))
        plt.plot(x, [spec_ceiling] * len(x), c="r")

print(f"Data Error No.: {data_error} pcs.")
print(f"Test Fail No.: {test_fail} pcs.")
print(f"Good Panel No.: {good_cnt} pcs.")
print(f"Total No.: {k} pcs.")

plt.show()