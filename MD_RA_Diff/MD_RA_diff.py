# to fetch and analyze MD data within the same file(befor/after RA)

import os
import time


import csv
import numpy as np
import progressbar
from mpl_toolkits import mplot3d


def MDrow(path):
    YMD = []
    XMD = []
    YMDline = 0
    XMDline = 0
    # fp = os.path.join(path, file)
    with open(path, "r") as f:
        iter_f = iter(f)
        #Find the index of differential
        for i, line in enumerate(iter_f):
            if "36) MicroDefect" in line:
                YMDline = i + 16
                XMDline = i + 12
    with open(path, "r") as f:
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
    # if len(YMD) == 0:
    #     print("Y MD is empty!")
    #     switch = False
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


    widgets = ['Progress: ', progressbar.Percentage(),
                ' ', progressbar.Bar('#'),' ', progressbar.Timer(),
                ' ', progressbar.ETA(),
                ' ', progressbar.FileTransferSpeed()]
    pbar = progressbar.ProgressBar(
        widgets=widgets, maxval=10*len(files_1)).start()


    k = 0
    with open(save_path, "a", newline='') as save_file:
        writer = csv.writer(save_file)
        writer.writerow(
            ['Judge(threshold)', 'Bar Code', 'Before RA', 'After RA',
            'X diff', 'Y diff ', 'X before', 'X after', 'Y before',
            'Y after'])

        for file in files_1:
            k += 1
            # print("")

            # fetch data from before RA
            fp_1 = os.path.join(file_Path_1, file)
            try:
                xmd_1, ymd_1 = MDrow(fp_1)
                xmd_1_array = np.array(xmd_1)
                ymd_1_array = np.array(ymd_1)
                # print(f"{file}\n{xmd_1_array}\n{ymd_1_array}")
            except:
                print(f"{file} MD ERROR!")

            # to match the data with after RA
            feature = sepName(file)
            for j, name in enumerate(files_2):
                if feature in name:
                    fp_2 = os.path.join(file_Path_2, files_2[j])
                    try:
                        xmd_2, ymd_2 = MDrow(fp_2)
                        xmd_2_array = np.array(xmd_2)
                        ymd_2_array = np.array(ymd_2)
                        file2 = files_2[j]
                        # print(f"{files_2[j]}\n{xmd_2_array}\n{ymd_2_array}")
                    except:
                        print(f"{files_2[j]} MD ERROR!")

            diff_x = xmd_2_array - xmd_1_array
            diff_y = ymd_2_array - ymd_1_array
            # print(diff, "\n")
            th = 1
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


if __name__ == "__main__":
    main()