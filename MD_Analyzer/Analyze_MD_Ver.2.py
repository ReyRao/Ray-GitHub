# !usr/bin/Python3
# to fetch and analyze the relation between micro defect and the comprehansive Cm
# touch IC: Solomon
# Rey
# Version 2

import os, sys
import pandas as pd
import numpy as np
import math
import csv

# path = "C:\\Users\\party\\Desktop\\MyGitHub\\Python\\data\\FAIL_Micro defect sorting"
path = "./Python/log/"
files = os.listdir(path)
for i in files:
    print(i)

uppermatrix = input("please enter the beginning row(of Cm matrix): ")
uppermatrix = int(uppermatrix)
bottommatrix = input("please enter the end row(of Cm matrix): ")
bottommatrix = int(bottommatrix)

print("\n")

# sfp = "C:\\Users\\party\\Desktop\\MyGitHub\\Python\\data\\save.csv"
sfp = "./Python/save.csv"
titledic = {"Title": ["File name", "Cm Mean", "Cm STD", "Test-1 (Max-Min < 1800)", "Test-2 (20500~23500)", "Test-3 (+15%/-10%)"]}
with open(sfp, "w", newline = "") as sf:
    writer = csv.writer(sf)
    for key, values in titledic.items():
        writer.writerows([values])

filelist = []
CmMean = []
STDlist = []  
Test1 = []
Test2 = []
Test3 = []

if (bottommatrix - uppermatrix) != 37:
    print("Wrong sensor line number!")

else:
    for filename in files:
        try:
            if os.path.splitext(filename)[-1] == ".csv":
                
                filelist = []
                CmMean = []
                STDlist = []  
                Test1 = []
                Test2 = []
                Test3 = []
                
                # print("".center(100, "-"))
                # print(filename.center(100, "-"))
                # print("".center(100, "-"))

                filelist.append(filename)

                # fp = path + "\\" + filename
                fp = os.path.join(path, filename)
                with open(fp, "r") as f:
                    lines = f.readlines()
                    total = []
                    total = (lines[uppermatrix-1:bottommatrix])
                # print(total[0], type(total))
        except:
            print(filename, ": cannot open!")

        try:
            def Mean(list):
                return sum(list)/len(list)

            def STD(list):
                return math.sqrt(sum((list - Mean(list)) ** 2) / len(list))

            total = [x.split() for x in total]
            # print(total[0], type(total))

            total = np.asarray(total)
            # print(total[0], type(total))

            df = pd.DataFrame(total)
            # print(df.head(), "\n", df.shape)
            
            df = df[0].str.split(",", expand = True)
            # print(df.head(), df.shape)

            # df = df.drop([0], axis = 1)
            # # print(df.head(), df.shape)
            # df = df.drop([52], axis = 1)
            print(df.head(), df.shape)
            df = pd.DataFrame(df.loc[:, 1:51])
        except:
            print(filename, "cannot be arranged!")

        try:
            for i in range(df.shape[1]):
                df[i+1] = pd.to_numeric(df[i+1])
            # print(df, df.dtypes)
            
            nor_df = df - 16384

            # print(nor_df.head())

            # print(nor_df.mean())

            # print(f"Overall mean value(-16384): {round(Mean(nor_df[0:].mean()), 2)}")
            
            meanresult = round(Mean(nor_df[0:].mean()), 2)
            CmMean.append(meanresult)

            # print(f"STD of Y-chennel: {round(STD(nor_df[0:].mean()), 2)}")
            
            STDresult = round(STD(nor_df[0:].mean()), 2)
            STDlist.append(STDresult)
        except:
            print(f"{filename} Mean & STD cannot be analized!")

        try:
            # print("".center(50, "-"))
            result1 = max(df.max()) - min(df.min())
            if (result1) < 1800:
                # print(f"Test 1 (Cm: Max-Min < 1800) Pass! (Cm: {round(result1, 2)})")
                Test1.append(f"Pass! (Cm: {round(result1, 2)})")
            elif (result1) >= 1800:
                # print(f"Test 1 (Cm: Max-Min < 1800) Fail! (Cm: {round(result1, 2)})")
                Test1.append(f"Fail! (Cm: {round(result1, 2)})")

            # print(df.shape)
            # print(df.iloc[0, 0], df.iloc[37, 50])

        except:
            print(f"{filename} Test1 cannot be analized!")

        try:
            index = 0
            nb = 0
            count = 0
            cnt2 = 0
            for j in range(df.shape[1]):
                for i in range(df.shape[0]):
                    nb += 1
                    if df.iloc[i, j] >= 23500 or df.iloc[i, j] <= 20500:
                        count += 1
                        cnt2 += 1
                        # print(f"Test 2 (20500~23500) Fail (Cm: {df.iloc[i, j]}) at column {j} No. {i}")
                        Test2.append(f"Fail! (Cm: {df.iloc[i, j]}) at column {j} No. {i}")
                    else:
                        next
                    
                index += 1
            if count == 0:
                # print("Test 2 (Cm:20500~23500) Pass!")
                Test2.append("Pass!")
        except:
            print(f"{filename} Test2 cannot be analized!")   
        
        try:
            index = 0
            nb = 0
            count = 0
            dfmean = round(Mean(df[0:].mean()), 2)
            nor_dfmean = round(Mean(nor_df[0:].mean()), 2)
            ub = round(Mean(nor_df[0:].mean()) * 0.15, 2)
            bb = round(Mean(nor_df[0:].mean()) * 0.1, 2)
            cnt3 = 0
            for j in range(df.shape[1]):
                for i in range(df.shape[0]):
                    nb += 1
                    if (df.iloc[i, j] - dfmean) >= 0:
                        if (df.iloc[i, j] - dfmean) >= ub:
                            cnt3 += 1
                            count += 1
                            # print(f"Test 3 (+15%/-10%) Fail (Cm: {round((df.iloc[i, j] - dfmean), 2)}) at column {j} No. {i}")
                            Test3.append(f"Fail({cnt3}) (Cm: {round((df.iloc[i, j] - dfmean), 2)}) at column {j} No. {i}")
                            
                    elif (df.iloc[i, j] - dfmean) <= 0:
                        if (df.iloc[i, j] - dfmean) <= -bb:
                            cnt3 += 1
                            count += 1
                            # print(f"Test 3 (+15%/-10%) Fail (Cm: {round((df.iloc[i, j] - dfmean), 2)}) at column {j} No. {i}")
                            Test3.append(f"Fail({cnt3}) (Cm: {round((df.iloc[i, j] - dfmean), 2)}) at column {j} No. {i}")
                            
                    else:
                        next
                    
                index += 1
            if count == 0:
                # print(f"Test 3 (Cm +15%/-10%) Pass!")
                Test3.append(f"Pass!")
        except:
            print(f"{filename} Test3 cannot be analized!")

        try:
            dic = {"key": [filelist[0], float(CmMean[0]), float(STDlist[0]), Test1[:], Test2[:], Test3[:]]}
            sfp = "./Python/save.csv"
            #sfp = "C:\\Users\\party\\Desktop\\MyGitHub\\Python\\data\\save.csv"
            with open(sfp, "a", newline = "") as sf:
                writer = csv.writer(sf)
                for key, value in dic.items():
                    writer.writerows([value])
        except:
            sfp = "./Python/save.csv"
            print(f"{filename}'s data cannot be saved!")
            errdic = {"errkey": [filename, "Wrong format!"]}
            with open(sfp, "a", newline = "") as sf:
                writer = csv.writer(sf)
                for key, values in errdic.items():
                    writer.writerows([values])

#print(df.head())