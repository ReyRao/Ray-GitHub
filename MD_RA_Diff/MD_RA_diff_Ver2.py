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
        for q, file in enumerate(files_1):
            k += 1
            data = []
            title = ['Judgement(Threshold)', 'max x MD (before RA)',
                    'max y MD (before RA)', 'max x MD (after RA)',
                    'max y MD (after RA)', 'Bar Code', 'Befoe RA',
                    'After RA']
            # fetch data from before RA
            fp_1 = os.path.join(file_Path_1, file)
            try:
                xmd_1, ymd_1 = MDrow(fp_1)
                xmd_1_array = np.asarray(xmd_1)
                ymd_1_array = np.asarray(ymd_1)
            except:
                print(f"{file} MD ERROR!")
                switch = False

            # x and y columns for before/after RA
            if q == 0:
                diff_x_title = [f"Diff X{i}-X{i+1}" for i in range(len(xmd_1_array))]
                diff_y_title = [f"Diff Y{i}-X{i+1}" for i in range(len(ymd_1_array))]
                x_title = [f"X{i}-X{i+1}" for i in range(len(xmd_1_array))]
                y_title = [f"Y{i}-X{i+1}" for i in range(len(ymd_1_array))]
                for i in range(len(x_title)):
                        title.append(diff_x_title[i])
                for i in range(len(y_title)):
                        title.append(diff_y_title[i])
                for i in range(2):
                    for i in range(len(x_title)):
                        title.append(x_title[i])
                for i in range(2):
                    for i in range(len(y_title)):
                        title.append(y_title[i])
                with open(save_path, 'a', newline='', encoding='utf8') as save_file:
                    writer = csv.writer(save_file)
                    writer.writerow(title)

            # to match the data with after RA
            if switch == True:
                feature = sepName(file)
                for j, name in enumerate(files_2):
                    if feature in name:
                        fp_2 = os.path.join(file_Path_2, files_2[j])
                        try:
                            xmd_2, ymd_2 = MDrow(fp_2)
                            xmd_2_array = np.asarray(xmd_2)
                            ymd_2_array = np.asarray(ymd_2)
                            file2 = files_2[j]
                        except:
                            print(f"{files_2[j]} MD ERROR!")
                            switch = False
                try:
                    diff_x = xmd_2_array - xmd_1_array
                    diff_y = ymd_2_array - ymd_1_array
                except:
                    print("DIFF ERROR!")
                    switch = False

            # print(diff, "\n")
            if switch == True:
                if len(diff_x[diff_x>th]) > 0 or len(diff_y[diff_y>th]) > 0:
                    judge = f'NG({th})'
                else:
                    judge = f'PASS({th})'

                diff_x = [float(f'{x:.2f}') for x in diff_x]
                diff_y = [float(f'{y:.2f}') for y in diff_y]
                data.append(judge)
                data.append(max(xmd_1_array))
                data.append(max(ymd_1_array))
                data.append(max(xmd_2_array))
                data.append(max(ymd_2_array))
                data.append(feature)
                data.append(file)
                data.append(file2)
                for i in range(len(diff_x)):
                    data.append(diff_x[i])
                for i in range(len(diff_y)):
                    data.append(diff_y[i])
                for i in range(len(xmd_1)):
                    data.append(xmd_1[i])
                for i in range(len(xmd_2)):
                    data.append(xmd_2[i])
                for i in range(len(ymd_1)):
                    data.append(ymd_1[i])
                for i in range(len(ymd_2)):
                    data.append(ymd_2[i])

                with open(save_path, 'a', newline='', encoding='utf8') as save_file:
                    writer = csv.writer(save_file)
                    writer.writerow(data)

                time.sleep(0.02)
                    
            pbar.update(10 * k)
            time.sleep(0.1)
        pbar.finish()

    if switch == False:
        os.remove(save_path)

    time.sleep(300)


if __name__ == "__main__":
    main()