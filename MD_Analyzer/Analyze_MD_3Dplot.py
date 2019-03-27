# !usr/bin/Python3
# -*- coding: UTF-8 -*-
# to analyze Solomon's the comprehensive Cm(full/half charge)
# Rey
# Version: 5

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
# from mpl_toolkits.mplot3d import Axes3D


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

def Mean(list):
    return round(sum(list) / len(list), 2)

def STD(list):
    return round(math.sqrt(sum((list - Mean(list)) ** 2) / len(list)), 3)

def remove(list, obj):
    return [x for x in list if x != obj]

def index(list, value):
    return [f"Y{i}-Y{i+1}" for i, x in enumerate(list) if x == value]

def pre_testCm(df):
        emp_cnt = 0
        if df.shape[0] != 38 and df.shape[1] != 51:
            switch = False
            emp_cnt += 1
            print(f"{file}'s shape is wrong! {df.shape[0], df.shape[1]}")
            err_list.append(f"{file}'s shape is wrong! {df.shape[0], df.shape[1]}")
        elif min(df.min()) < 16384:
            switch = False
            print(f"{file} have to be confirmed again!")
            err_list.append(f"{file} have to be confirmed again!")
            # os.rename(os.path.join(path, file), os.path.join(path, "confirm_again_" + file))
        else:
            switch = True
        return switch, emp_cnt

def pre_testHCm(df):
        if df.shape[0] != 38 and df.shape[1] != 51:
            switch = False
            print(f"{file}'s shape is wrong! {df.shape[0], df.shape[1]}")
            err_list.append(f"{file}'s shape is wrong! {df.shape[0], df.shape[1]}")
        elif min(df.min()) < 16384:
            switch = False
            print(f"{file} have to be confirmed again!")
            err_list.append(f"{file} have to be confirmed again!")
            os.rename(os.path.join(path, file), os.path.join(path, "confirm_again_" + file))
        else:
            switch = True
        return switch

def dosomework():
    time.sleep(0.01)

def MDrow(path):
    YMD = []
    XMD = []
    YMDline = 0
    XMDline = 0
    switch = True
    fp = os.path.join(path, file)
    with open(fp, "r") as f:
        iter_f = iter(f)
        #Find the index of differential
        for i, line in enumerate(iter_f):
            if "36) MicroDefect" in line:
                XMDline = i + 12
                YMDline = i + 16
    with open(fp, "r") as f:
        rows = f.readlines()
        YMD = rows[YMDline]
        # print(YMD)
        YMD = YMD.replace("%", "")
        YMD = YMD.replace("Diff", "")
        YMD = YMD.replace(",", " ")
        YMD = [float(x) for x in YMD.split()]
        # print(YMD, index(YMD, max(YMD)))
    
    if len(YMD) == 0:
        print("Y MD is empty!")
        switch = False

    return YMD, switch

def countMD(list, Th):
    i = 0.0
    for x in list:
        if x >= Th:
            i += 1
    return i

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

def Test_3(df):
    dfmean = round(Mean(df[0:].mean()), 2)
    ub = round(Mean(df[0:].mean()) * 0.15, 2)
    bb = round(Mean(df[0:].mean()) * 0.1, 2)
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

print("".center(100, "="))

path = "./Python/log/"
spath = "./Python/save.xlsx"
err = "./Python/err.xlsx"

files = os.listdir(path)

prewrite = {
    "test":[0]
}
predf = pd.DataFrame(prewrite)

try:
    predf.to_excel(spath, sheet_name="Sheet_1")
    
except PermissionError:
    print("Please close save.xlsx and re-run the program!")

# CmUpper = input("Please enter the first row of full-charge Cm: ")
CmUpper = 66
CmUpper = int(CmUpper)
CmBottom = CmUpper + 37

# hCmUpper = input("Please enter the first row of half-charge Cm: ")
hCmUpper = 116
hCmUpper = int(hCmUpper)
hCmBottom = hCmUpper + 37

# YMDTh = input("Please input Y MicroDefect threshold(%): ")
YMDTh = 10
YMDTh = float(YMDTh)
YMDlist = []
YMDmaxIndex = []
YMDcount_list = []
file_list = []
Test_1_count_list = []
Test_2_count_list = []
Test_3_count_list = []
fMean = []
hMean = []
CmSTDlist = []
hCmSTDlist = []
diffSTDlist = []
sum12cntlist = []
sum123cntlist = []
err_list = []
RMClist = []
RSTDClist = []
x_pass_fitlist = []
y_pass_fitlist = []
z_pass_fitlist = []
x_fail_fitlist = []
y_fail_fitlist = []
z_fail_fitlist = []


widgets = ['Progress: ',Percentage(), ' ', Bar('#'),' ', Timer(),
        ' ', ETA(), ' ', FileTransferSpeed()]
pbar = ProgressBar(widgets=widgets, maxval=10*len(files)).start()

switch = False
empty_cnt = 0
MD_cnt = 0
k = 0
for file in files:
    k += 1
    fp = os.path.join(path, file)
    try:
        CmTb = makeDf(fp, CmUpper, CmBottom)
        mCmTb = CmTb - 16384
        
    except:
        print(f"{file} Full-charge Cm cannot be arranged!")
        err_list.append(f"{file} Full-charge Cm cannot be arranged!")
        switch = False


    try:
        hCmTb = makeDf(fp, hCmUpper, hCmBottom)
        hmCmTb = hCmTb - 16384

    except:
        print(f"{file} Half-charge Cm cannot be arranged!")
        err_list.append(f"{file} Half-charge Cm cannot be arranged!")
        switch = False


    try:
        switch, emp_cnt = pre_testCm(CmTb)
        switch = pre_testHCm(hCmTb)
        empty_cnt += emp_cnt

    except ValueError:
        print(f"{file} min() arg is an empty sequence")
        err_list.append(f"{file} min() arg is an empty sequence")


    try:
        if switch == True:
            YMD, switch = MDrow(path)
            # print(f"YMD: {YMD}", "\n")
        else:
            print(f"{file} MD can't be analyzed!")
            err_list.append(f"{file} MD can't be analyzed!")
            switch = False

    except:
        print(f"{file} Micro Defect row cannot be arranged!")
        err_list.append(f"{file} Micro Defect row cannot be arranged!")
        MD_cnt += 1
        switch = False
        # os.rename(os.path.join(path, file), os.path.join(path, "Uncompleted_" + file))
    

    if switch == True:
        YMDlist.append(max(YMD))
        YMDmaxIndex.append(index(YMD, max(YMD))[0])
        YMDcount_list.append(countMD(YMD, YMDTh))
        file_list.append(file)

        try:
            meanccf = 0
            meanccf = np.corrcoef(mCmTb.mean(), hmCmTb.mean())
            RMClist.append(meanccf[1, 0])

        except:
            print(f"{file} mean corrcoef err!")
            err_list.append(f"{file} mean corrcoef err!")

        
        try:
            STDccf = 0
            STDccf = np.corrcoef(mCmTb.std(), hmCmTb.std())
            RSTDClist.append(STDccf[1, 0])

        except:
            print(f"{file} STD corrcoef err!")
            err_list.append(f"{file} STD corrcoef err!")


        try:
            hMean.append(Mean(hCmTb.mean()))
            fMean.append(Mean(CmTb.mean()))
        except:
            print(f"{file} mean err!")
            err_list.append(f"{file} mean err!")


        try:
            CmSTD = STD(CmTb.mean())
            CmSTDlist.append(CmSTD)
            hCmSTD = STD(hCmTb.mean())
            hCmSTDlist.append(hCmSTD)
            # diffSTD = abs((hCmSTD - CmSTD) / hCmSTD)
            # diffSTDlist.append(diffSTD)

        except:
            print(f"{file} STD err!")
            err_list.append(f"{file} STD err!")


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
            Test_3_count = Test_3(mCmTb)
            Test_3_count_list.append(Test_3_count)

        except:
            print(f"{file} Test_3 cannot be analyzed")
            err_list.append(f"{file} test_3 cannot be analyzed!")

        x = np.linspace(1, 51, 51)
        y = np.array(mCmTb.mean())
        fit = np.polyfit(x, y, 2)
        
        try:
            cnt12 = 0
            cnt123 = 0
            if Test_1_count == 0 and Test_2_count == 0 and Test_3_count == 0:
                cnt123 += 1
                x_pass_fitlist.append(fit[0])
                y_pass_fitlist.append(fit[1])
                z_pass_fitlist.append(fit[2])

                # os.rename(os.path.join(path, file), os.path.join(path, "passFromProgram_" + file))
            else:
                x_fail_fitlist.append(fit[0])
                y_fail_fitlist.append(fit[1])
                z_fail_fitlist.append(fit[2])

                # os.rename(os.path.join(path, file), os.path.join(path, "failFromProgram_" + file))

            if Test_1_count == 0 and Test_2_count == 0:
                cnt12 += 1

            sum12cntlist.append(cnt12)
            sum123cntlist.append(cnt123)

        except:
            print(f"{file} count wrong!")
            err_list.append(f"{file} count wrong!")
                
    else:
        print(f"{file} is empty!")
        err_list.append(f"{file} is empty!")
    
    pbar.update(10 * k)
    dosomework()
pbar.finish()


# ax = plt.axes(projection = "3d")
# ax.scatter3D(x_pass_fitlist, y_pass_fitlist, z_pass_fitlist, s=100)
# ax.scatter3D(x_fail_fitlist, y_fail_fitlist, z_fail_fitlist)
# plt.title("Statistic")
# plt.xlabel("coef. C1")
# plt.ylabel("coef. C2")
# ax.set_zlabel("coef. C3")
# plt.legend("Pass Sample", "Fail Sample")

# plt.scatter(x, y)
# plt.ylim(4000, 8000)
# linefit = np.polyfit(x, y, 2)
# yval = np.poly1d(linefit)
# print(yval)
# plt.plot(x, yval(x))

# plt.show()


print("Saving the data now...")

CmDic = {
    "filename": file_list,
    "100% Cm mean": fMean,
    "50% Cm mean": hMean,
    "Row mean corrcoef": RMClist,
    "50% Cm STD": hCmSTDlist,
    "100% Cm STD": CmSTDlist,
    "Row STD corrcoef": RSTDClist,
    "Y_MD_No.": YMDcount_list,
    "Line Y maxMD": YMDmaxIndex,
    "Y maxMD": YMDlist,
    "100% Test 1": Test_1_count_list,
    "100% Test 2": Test_2_count_list,
    "100% Test 3": Test_3_count_list,
    "100% 1&2": sum12cntlist,
    "100% 1&2&3": sum123cntlist
    }

err_dict = {
    "Error": err_list
    }


print("".center(100, "="))
print(f"{empty_cnt} empty file(s)!")
print(f"{MD_cnt} MD data err file(s)!")

df = pd.DataFrame(CmDic)
df = df.sort_values(by = ["Y maxMD"])
print(df.head(), "\n", df.shape, "\n", df.describe())

err_df = pd.DataFrame(err_dict)
err_df.to_excel(err, sheet_name="Sheet_1")


try:
    df.to_excel(spath, sheet_name="Sheet_1")
except PermissionError:
    print("Please close the save data!")

print("This program will be stopped in 5 seconds...")




###########################################################################################

data = np.asarray(mCmTb).flatten()
xline = np.linspace(1, 38, 38)
yline = np.linspace(1, 51, 51)
x_line = []
y_line = []
for i in range(51):
    x_line = np.append(x_line, xline)
for i in range(38):
    y_line = np.append(y_line, yline)

print(f"len(data), len(x_line), len(y_line){len(data), len(x_line), len(y_line)}")
total_data = np.c_[x_line, y_line, data]

print(f"total_data shape: {total_data.shape}")

# regular grid covering the domain of the data
X,Y = np.meshgrid(np.arange(1, 38.5, 0.5), np.arange(1, 51.5, 0.5))

# print(X, "\n", "\n", Y)

XX = X.flatten()
YY = Y.flatten()
print(f"X: {X.shape}")
print(f"XX: {XX.shape}")


order = 2    # 1: linear, 2: quadratic
if order == 1:
    # best-fit linear plane
    A = np.c_[total_data[:,0], total_data[:,1], np.ones(total_data.shape[0])]
    C,_,_,_ = scipy.linalg.lstsq(A, total_data[:,2])    # coefficients

    # print(C)

    # evaluate it on grid
    Z = C[0]*X + C[1]*Y + C[2]

    # or expressed using matrix/vector product
    #Z = np.dot(np.c_[XX, YY, np.ones(XX.shape)], C).reshape(X.shape)

elif order == 2:
    # best-fit quadratic curve
    A = np.c_[np.ones(total_data.shape[0]), total_data[:,:2], np.prod(total_data[:,:2], axis=1), total_data[:,:2]**2]
    C,_,_,_ = scipy.linalg.lstsq(A, total_data[:,2])

    # print(A, "\n", "\n", C)

    # evaluate it on a grid
    Z = np.dot(np.c_[np.ones(XX.shape), XX, YY, XX*YY, XX**2, YY**2], C).reshape(X.shape)
    print(np.c_[np.ones(XX.shape), XX, YY, XX*YY, XX**2, YY**2].shape)

# plot points and fitted surface
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, alpha=0.2)
ax.scatter(total_data[:,0], total_data[:,1], total_data[:,2], c='r', s=10)
plt.xlabel('X')
plt.ylabel('Y')
ax.set_zlabel('Cm')
ax.axis('equal')
ax.axis('tight')
plt.show()