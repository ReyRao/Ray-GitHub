#!usr/bin/python3
# file_name/Fail or Pass/how many fail/MD X, Y line

import os, sys
import pandas as pd
import numpy as np
import time
from progressbar import *

def dosomework():
    time.sleep(0.01)

def MDrow(path):
    YMD = []
    XMD = []
    YMDline = 0
    XMDline = 0
    switch = True
    fp = os.path.join(path, file_name)
    with open(fp, "r") as f:
        iter_f = iter(f)
        #Find the index of differential
        for i, line in enumerate(iter_f):
            if "MicroDefect" in line:
                YMDline = i + 16
                XMDline = i + 12
    with open(fp, "r") as f:
        rows = f.readlines()
        YMD = rows[YMDline]
        YMD = YMD.replace("%", "")
        YMD = YMD.replace("Diff", "")
        YMD = YMD.replace(",", " ")
        YMD = [float(x) for x in YMD.split()]
        XMD = rows[XMDline]
        XMD = XMD.replace("%", "")
        XMD = XMD.replace("Diff", "")
        XMD = XMD.replace(",", " ")
        XMD = [float(x) for x in XMD.split()]
    if len(XMD) == 0:
        print("MD is empty!")
        switch = False
    return XMD, YMD, switch


Xth = input("Please set X threshold(default=0):\n")
if Xth != "":
    Xth = int(Xth)
else:
    Xth = 0

Yth = input("Please set Y threshold(default=0):\n")
if Yth != "":
    Yth = int(Yth)
else:
    Yth = 0

path = r'log/'
files = os.listdir(path)

X_total_df = pd.DataFrame()
Y_total_df = pd.DataFrame()
X_final_df = pd.DataFrame()
Y_final_df = pd.DataFrame()
xcount_df = pd.DataFrame()
ycount_df = pd.DataFrame()
file_name_list = []
global X_length
global Y_length
xjudge_list = []
yjudge_list = []
xcount_list = []
ycount_list = []

widgets = ['Progress: ',Percentage(), ' ', Bar('#'),' ', Timer(),
        ' ', ETA(), ' ', FileTransferSpeed()]
pbar = ProgressBar(widgets=widgets, maxval=10*len(files)).start()
k = 0
for file_name in files:
    k += 1
    xjudge = 'PASS'
    xcount = 0
    yjudge = 'PASS'
    ycount = 0
    file_name_list.append(file_name)
    XMD, YMD, switch = MDrow(path)

    for value in XMD:
        if Xth <= value:
            xjudge = "FAIL"
            xcount += 1
    xjudge_list.append(xjudge)
    xcount_list.append(xcount)

    for value in YMD:
        if Yth <= value:
            yjudge = "FAIL"
            ycount += 1
    yjudge_list.append(yjudge)
    ycount_list.append(ycount)

    X_length = len(XMD)
    Y_length = len(YMD)
    X_df = pd.DataFrame(XMD)
    X_df = X_df.transpose()
    Y_df = pd.DataFrame(YMD)
    Y_df = Y_df.transpose()
    X_total_df = X_total_df.append(X_df)
    Y_total_df = Y_total_df.append(Y_df)

    pbar.update(10 * k)
    dosomework()
pbar.finish()

X_title = [f'X{i}-X{i+1}' for i in range(X_length)]
X_total_df.columns = X_title
Y_title = [f'Y{i}-Y{i+1}' for i in range(Y_length)]
Y_total_df.columns = Y_title

X_total_df.index = file_name_list
Y_total_df.index = file_name_list

xcount_df = pd.DataFrame(xcount_list, index=file_name_list, columns=['Over #'])
ycount_df = pd.DataFrame(ycount_list, index=file_name_list, columns=['Over #'])
X_final_df = pd.concat([xcount_df, X_total_df], axis=1)
Y_final_df = pd.concat([ycount_df, Y_total_df], axis=1)

xjudge_df = pd.DataFrame(xjudge_list, index=file_name_list, columns=['PASS/FAIL'])
yjudge_df = pd.DataFrame(yjudge_list, index=file_name_list, columns=['PASS/FAIL'])
X_final_df = pd.concat([xjudge_df, X_final_df], axis=1)
Y_final_df = pd.concat([yjudge_df, Y_final_df], axis=1)


# print("\n", X_final_df.head())
# print("\n", Y_final_df.head())
X_final_df.to_csv(os.path.join('./', "X_MicroDefect.csv"))
Y_final_df.to_csv(os.path.join('./', "Y_MicroDefect.csv"))