#!usr/bin/python3
# file_name/Fail or Pass/how many fail/MD X, Y line

import os, sys
import pandas as pd
import numpy as np
import time
from progressbar import *

def dosomework():
    time.sleep(0.01)

class AnalyzeMD():
    def __init__(self, path):
        self.path = path
        self.md = []

    # XMDline is "i+12"
    # YMDline is "i+16"
    def MDrow(self, lineNumber):
        self.lineNumber = lineNumber
        MDline = 0
        fp = os.path.join(path, file_name)
        with open(fp, "r") as f:
            iter_f = iter(f)
            #Find the index of differential
            for i, line in enumerate(iter_f):
                if "MicroDefect" in line:
                    MDline = i + lineNumber
        with open(fp, "r") as f:
            rows = f.readlines()
            self.md = rows[MDline]
            self.md = self.md.replace("%", "")
            self.md = self.md.replace("Diff", "")
            self.md = self.md.replace(",", " ")
            self.md = [float(x) for x in self.md.split()]
        return self.md

    def judge_count(self, th):
        self.th = th
        judge = 'PASS'
        count = 0
        for value in self.md:
            if th <= value:
                judge = "FAIL"
                count += 1
        return judge, count


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

# detect saving data
savingDataCheck = False
try:
    saving_test_df = pd.DataFrame()
    saving_test_df.to_csv(os.path.join('./', "X_MicroDefect.csv"))
    savingDataCheck = True
except:
    print('Plz close X_MicroDefect.csv and execute again !!!')
    savingDataCheck = False

if savingDataCheck == True:
    try:
        saving_test_df = pd.DataFrame()
        saving_test_df.to_csv(os.path.join('./', "Y_MicroDefect.csv"))
        savingDataCheck = True
    except:
        print('Plz close Y_MicroDefect.csv and execute again !!!')
        savingDataCheck = False


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

if savingDataCheck == True:
    for file_name in files:
        k += 1
        test = False

        # to get X, Y MicroDefect rows
        try:
            X = AnalyzeMD(path)
            XMD = X.MDrow(12)
            test = True
        except:
            print(f'Analyzing X-line MicroDefect is Fail at {file_name}')
            test = False
        
        if test == True:
            try:
                Y = AnalyzeMD(path)
                YMD = Y.MDrow(16)
                test = True
            except:
                print('Analyzing Y-line MicroDefect is Fail at %s' %file_name)
                test = False

        if test == True:
            try:
                xjudge, xcount = X.judge_count(Xth)
                xjudge_list.append(xjudge)
                xcount_list.append(xcount)
                test = True
            except:
                print('%s X-line judge and count fail' %file_name)
                test = False

        if test == True:
            try:
                yjudge, ycount = Y.judge_count(Yth)
                yjudge_list.append(yjudge)
                ycount_list.append(ycount)
                test = True
            except:
                print('%s Y-line judge and count fail' %file_name)
                test = False
        
        # append saving data
        if test == True:
            try:
                file_name_list.append(file_name)
                X_length = len(XMD)
                Y_length = len(YMD)
                X_df = pd.DataFrame(XMD)
                X_df = X_df.transpose()
                Y_df = pd.DataFrame(YMD)
                Y_df = Y_df.transpose()
                X_total_df = X_total_df.append(X_df)
                Y_total_df = Y_total_df.append(Y_df)
            except:
                print('{} final append ERROR!'.format(file_name))

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