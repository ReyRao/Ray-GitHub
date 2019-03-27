# !usr/bin/Python3
# to fetch and analyze the relation between micro defect and the comprehansive Cm
# Touch IC: Solomon
# Rey
# Version 3

import numpy as np
import pandas as pd
import os, sys
import csv
import time
from progressbar import *


def Mean(list):
    return sum(list) / len(list)

def remove(list, obj):
    return [x for x in list if x != obj]

def index(list, value):
    return [f"Y{i}-Y{i+1}" for i, x in enumerate(list) if x == value]

def dosomework():
    time.sleep(0.01)

def countMD(list, Th):
    i = 0.0
    for x in list:
        if x >= Th:
            i += 1
    return i

print("".center(100, "="))

path = "./Python/log/"
spath = "./Python/save.xlsx"

files = os.listdir(path)
# for i, j in enumerate(files):
#     print(f"{i+1}. {j}")

CmUpper = input("Please enter the first row of Cm: ")
CmUpper = int(CmUpper)
CmBottom = CmUpper + 38

YMDTh = input("Please input Y MicroDefect threshold(%): ")
YMDTh = float(YMDTh)
YMDlist = []
YMDmaxIndex = []
YMDcount_list = []

# XMDlist = []
# XMDmaxIndex = []

file_list = []
Test_1_count_list = []
Test_2_count_list = []
Test_3_count_list = []
switch = False
empty_cnt = 0

widgets = ['Progress: ',Percentage(), ' ', Bar('#'),' ', Timer(),
        ' ', ETA(), ' ', FileTransferSpeed()]
pbar = ProgressBar(widgets=widgets, maxval=10*len(files)).start()

k = 0
for file in files:
    k += 1
    try:
        # print(file.center(100, "="))
        fp = os.path.join(path, file)
        with open(fp, "r") as f:
            rows = f.readlines()
            CmTb = []
            CmTb = (rows[CmUpper - 1:CmBottom])
            CmTb = [x.split() for x in CmTb]
            # CmTb = np.asarray(CmTb)
            # print(CmTb)
            # print("".center(50, "-"))
            CmTb = pd.DataFrame(CmTb)
            # print(CmTb.head())
            # print("".center(50, "-"))
            CmTb = CmTb[0].str.split(",", expand = True)
            # print(CmTb.head())
            # print("".center(50, "-"))
            CmTb = pd.DataFrame(CmTb.loc[:, 1:51])
            # print(CmTb.head())
            for i in range(CmTb.shape[1]):
                    CmTb[i+1] = pd.to_numeric(CmTb[i+1])
            # print(CmTb.dtypes)
            mCmTb = CmTb - 16384
            # print(mCmTb.head())

    except:
        print(f"{file}cannot be arranged!")

    try:
        if CmTb.shape[0] != 38 and CmTb.shape[1] != 51:
            switch = False
            empty_cnt += 1
            print(f"{file}'s shape is wrong! {CmTb.shape[0], CmTb.shape[1]}")
        elif min(CmTb.min()) < 16384:
            switch = False
            print(f"{file} have to be confirmed again!")
            os.rename(os.path.join(path, file), os.path.join(path, "Need to be confirmed_" + file))
        else: 
            switch = True

    except ValueError:
        print(f"{file} min() arg is an empty sequence")


    if switch == True:
        try:
            YMD = []
            XMD = []
            YMDline = 0
            XMDline = 0
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
                YMD.append(rows[YMDline])
                # print(YMD)
                YMD = "".join(str(x) for x in YMD)
                # print(YMD)
                YMD = YMD.replace("%", "")
                YMD = YMD.replace("Diff", "")
                YMD = YMD.replace(",", " ")
                YMD = [float(x) for x in YMD.split()]
                # print(YMD, index(YMD, max(YMD)))
                YMDlist.append(max(YMD))
                YMDmaxIndex.append(index(YMD, max(YMD))[0])
                YMDcount_list.append(countMD(YMD, YMDTh))

        except:
            print(f"{file} Micro Defect row cannot be arranged!")
            os.rename(os.path.join(path, file), os.path.join(path, "empty_MD_" + file))
            

        file_list.append(file)

        Test_1_count = 0
        try:
            # print("".center(50, "-"))
            result1 = max(CmTb.max()) - min(CmTb.min())
            if (result1) < 1800:
                # print(f"Test 1 (Cm: Max-Min < 1800) Pass! (Cm: {round(result1, 2)})")
                Test_1_count += 0

            elif (result1) >= 1800:
                # print(f"Test 1 (Cm: Max-Min < 1800) Fail! (Cm: {round(result1, 2)})")
                Test_1_count += 1
            
            Test_1_count_list.append(Test_1_count)
        
        except:
            print(f"{file} test_1 cannot be analyzed!")

        Test_2_count = 0
        try:
            for j in range(CmTb.shape[1]):
                for i in range(CmTb.shape[0]):
                    if CmTb.iloc[i, j] >= 23500 or CmTb.iloc[i, j] <= 20500:
                        Test_2_count += 1
                    else:
                        Test_2_count += 0

            Test_2_count_list.append(Test_2_count//38)

        except:
            print(f"{file} Test2 cannot be analyzed!")  

        Test_3_count = 0
        try:
            CmTbmean = round(Mean(CmTb[0:].mean()), 2)
            mCmTbmean = round(Mean(mCmTb[0:].mean()), 2)
            ub = round(Mean(mCmTb[0:].mean()) * 0.15, 2)
            bb = round(Mean(mCmTb[0:].mean()) * 0.1, 2)
            for j in range(CmTb.shape[1]):
                for i in range(CmTb.shape[0]):
                    if (CmTb.iloc[i, j] - CmTbmean) >= 0:
                        if (CmTb.iloc[i, j] - CmTbmean) >= ub:
                            Test_3_count += 1
                    elif (CmTb.iloc[i, j] - CmTbmean) <= 0:
                        if (CmTb.iloc[i, j] - CmTbmean) <= -bb:
                            Test_3_count += 1
                    else:
                        Test_3_count += 0

            Test_3_count_list.append(Test_3_count//38)

        except:
            print(f"{file} Test3 cannot be analyzed")
        
    else:
        print(f"{file} is empty!")
    
    pbar.update(10 * k)
    dosomework()
pbar.finish()

# print(f"file_list:\n {file_list}")
# print(f"Test_1_count_list: {Test_1_count_list}")
# print(f"Test_2_count_list: {Test_2_count_list}")
# print(f"Test_3_count_list: {Test_3_count_list}")
dic = {
    "filename": file_list,
    "Y_MD_No.": YMDcount_list,
    "Line_Y_maxMD": YMDmaxIndex,
    "Y_maxMD": YMDlist,
    "Test_1": Test_1_count_list,
    "Test_2": Test_2_count_list,
    "Test_3": Test_3_count_list
    }

pbar.update(10 * k)
dosomework()
pbar.finish()

df = pd.DataFrame(dic)
df = df.sort_values(by = ["Y_maxMD"])
print(df.head(), "\n", df.shape, "\n", df.describe())

print("".center(100, "="))
print(f"There are {empty_cnt} empty files!")

df.to_excel(spath, sheet_name="Sheet_1")