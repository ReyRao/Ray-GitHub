#!user/bin/python3
# -*- coding: utf-8 -*-
# to fetch and analyze MD data within the same file(befor/after RA)
# disqus: Rey

import os
import time


import csv
import numpy as np
import progressbar


def MDrow(path):
    YMD = []
    XMD = []
    YMDline = 0
    XMDline = 0
    # fp = os.path.join(path, file)
    with open(path, "r", encoding='utf8') as f:
        iter_f = iter(f)
        #Find the index of differential
        for i, line in enumerate(iter_f):
            if "36) MicroDefect" in line:
                YMDline = i + 16
                XMDline = i + 12
    with open(path, "r", encoding='utf8') as f:
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
    if len(YMD) < 0:
        print("Y MD is empty!")
    if len(XMD) < 0:
        print("X MD is empty!")
    return XMD, YMD


def sepName(file_name):
    name = file_name.split('_')
    return name[1]

def main():
    file_Path_1 = "./beforeRA/"
    file_Path_2 = "./afterRA/"
    save_path = "./diff_data.csv"

    files_1 = os.listdir(file_Path_1)
    files_2 = os.listdir(file_Path_2)

    th = float(input("Plz input a threshold value you want:\n"))

    switch = True

    try:
        with open(save_path, "w+", encoding='utf8') as cleanFile:
            cleanFile.close()
    except:
        print('Plz close the saving file!')
        switch = False

    if switch == True:
        widgets = ['Progress: ', progressbar.Percentage(),
                    ' ', progressbar.Bar('#'),' ', progressbar.Timer(),
                    ' ', progressbar.ETA(),
                    ' ', progressbar.FileTransferSpeed()]
        pbar = progressbar.ProgressBar(
            widgets=widgets, maxval=10*len(files_1)).start()


        k = 0
        with open(save_path, "a", newline='', encoding='utf8') as save_file:
            writer = csv.writer(save_file)
            writer.writerow(
                ['Judge(threshold)', 'Bar Code', 'Before RA', 'After RA',
                'X diff', 'Y diff ', 'X before', 'X after', 'Y before',
                'Y after'])

            for file in files_1:
                k += 1

                # fetch data from before RA
                fp_1 = os.path.join(file_Path_1, file)
                try:
                    xmd_1, ymd_1 = MDrow(fp_1)
                except:
                    print(f"{file} MD ERROR!")
                    switch = False

                try:
                    xmd_1_array = np.asarray(xmd_1)
                    ymd_1_array = np.asarray(ymd_1)
                except:
                    print(f"{file} nparray ERROR!")
                    switch = False

                # to match the data with after RA
                if switch == True:
                    feature = sepName(file)
                    for j, name in enumerate(files_2):
                        if feature in name:
                            fp_2 = os.path.join(file_Path_2, files_2[j])
                            try:
                                xmd_2, ymd_2 = MDrow(fp_2)
                            except:
                                print(f"{files_2[j]} MD ERROR!")
                                switch = False

                            try:
                                xmd_2_array = np.asarray(xmd_2)
                                ymd_2_array = np.asarray(ymd_2)
                                file2 = files_2[j]
                                # print(f"{files_2[j]}\n{xmd_2_array}\n{ymd_2_array}")
                            except:
                                print(f"{files_2[j]} nparray ERROR!")
                                switch = False

                    try:
                        diff_x = xmd_2_array - xmd_1_array
                        diff_y = ymd_2_array - ymd_1_array
                    except:
                        print("DIFF ERROR!")
                        switch = False

                # print(diff, "\n")
                if switch == True:
                    if len(diff_x[diff_x>th]) > 0 and len(diff_y[diff_y>th]) > 0:
                        judge = f'NG({th})'
                    else:
                        judge = f'PASS({th})'

                    diff_x = [float(f'{x:.2f}') for x in diff_x]
                    diff_y = [float(f'{y:.2f}') for y in diff_y]

                    writer.writerow(
                        [judge, feature, file, file2, diff_x,
                        diff_y, xmd_1, xmd_2, ymd_1, ymd_2])
                    time.sleep(0.02)

                        
                pbar.update(10 * k)
                time.sleep(0.1)
            pbar.finish()

    if switch == False:
        os.remove(save_path)

    time.sleep(3600)


if __name__ == "__main__":
    main()