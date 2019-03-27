#   For Wacom G12+
#   To calculate linearity
#       1. Max deviation position
#       2. Standar deviation
#   Data structure: Wacom G12+
#   Python 3
#   Ray
#   Version: Ver.2
#
#####################################
import os, sys
import math
import numpy as np

path = "C:\\Users\\party\\Desktop\\Ray\\WacomG12plus\\Linearity\\Raw_data"

files = os.listdir(path)
print(files)

filename = input("whitch data: ")
deletenum = input("How many points of data(pen down/up) you want to delete: ")
deletenum = int(deletenum)

def remove_from_list(the_list, obj):
    return[x for x in the_list if x != obj]

X = []
Y = []
with open(path + "\\" + filename, "r") as f:
    for line in f:
        try:
            X.append(line.split(",")[0][2:])
            Y.append(line.split(",")[1][3:])
        except IndexError:
            print(line, "never mind")
print("\n")

X = remove_from_list(X, "p=0\n")
X = remove_from_list(X, "p=1\n")
X = remove_from_list(X, "p=0")
X = [int(x) for x in X]
Y = [int(y) for y in Y]

#print("\n", "X coordinate: ", "\n", X, "\n", "X total  elements: ", len(X))
#print("\n", "Y coordinate: ", "\n", Y, "\n", "Y total elements: ", len(Y))

tmp = []
for i in range(len(X) -1):
    if abs(X[i] - X[i+1]) > 500 or abs(Y[i] - Y[i+1]) > 500:
        tmp.append(i+1)
tmp.append(len(X))
#print("\n", tmp, "\n")

ntmp = [tmp[0] - 2 * deletenum]
for i in range(1, len(tmp)):
    ntmp.append((tmp[i] - tmp[i - 1]) - 2 * deletenum)
#print(ntmp, "\n")

Xavr = []
Xavr.append(sum(X[deletenum:tmp[0] - deletenum]) / ntmp[0])
Yavr = []
Yavr.append(sum(Y[deletenum:tmp[0] - deletenum]) / ntmp[0])
for i in range(1, len(tmp)):
    Xavr.append(sum(X[tmp[i - 1] + deletenum:tmp[i] - deletenum]) / ntmp[i])
    Yavr.append(sum(Y[tmp[i - 1] + deletenum:tmp[i] - deletenum]) / ntmp[i])

#print("X average: ", Xavr)
#print("Y average: ", Yavr)

#Linear Regression
X = np.asarray(X)
Y = np.asarray(Y)
Xavr = np.asarray(Xavr)
Yavr = np.asarray(Yavr)

Xarry = []
Xarry.append(X[deletenum:tmp[0] - deletenum])
Yarry = []
Yarry.append(Y[deletenum:tmp[0] - deletenum])
for i in range(1, len(ntmp)):
    Xarry.append(X[tmp[i - 1] + deletenum:tmp[i] - deletenum])
    Yarry.append(Y[tmp[i - 1] + deletenum:tmp[i] - deletenum])

au = []
ad = []
a = []
b = []
D0 = []
AD = []
SD = []
TXarry = 0
for i in range(len(tmp)):
    au.append((Xarry[i] - Xavr[i]) * (Yarry[i] - Yavr[i]))
    ad.append((Xarry[i] - Xavr[i]) ** 2)
    a.append(sum(au[i])/sum(ad[i]))
    #print(sum(au[i]), "    ", sum(ad[i]), "    ", "\n", "a: ", a[i])
    b.append(Yavr[i] - a[i] * Xavr[i])
    #print("b: ", b[i])
    D0.append(abs(Yarry[i] - a[i] * Xarry[i] - b[i]) / (1 + a[i]**2) ** (.5))
    #print("Do: ", D0[i], "\n")
    AD.append(sum(D0[i]) / ntmp[i])
    SD.append((sum((D0[i]-AD[i]) ** 2) / ntmp[i]) ** (.5))
    (m, j) = max((v, j) for j, v in enumerate(D0[i]))
    print("Line ", i + 1, ": ")
    print("Data size: ", len(Xarry[i]))
    TXarry += len(Xarry[i])
    print("Max Deviation at (x, y): (", Xarry[i][j],", ", Yarry[i][j], ")")
    print("Average Deviation(in micrometer): ", AD[i]*10, "\n", "3 * Standard Deviation(in micrometer): ", SD[i]*30)
    print("Max deviation(in micrometer): ", max(D0[i])*10, "\n")

# for i in range(len(tmp)):
#     print(SD[i] * 30)
