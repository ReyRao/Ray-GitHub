#   For Wacom G12+
#   To calculate accuracy
#   Data structure: Wacom G12+
#   Python 3
#   Ray
#   Version: Ver.1
#
###################################################

import os, sys
import numpy as np
import math

path = "C:\\Users\\user\\Desktop\\Ray\\WacomG12plus\\Linearity"
files = os.listdir(path)
print(files)

filename = input("data: ")
deletenum = 0

def remove_from_list(the_list, obj):
    return[x for x in the_list if x != obj]

X = []
Y = []
with open(path + "\\" + filename, "r") as file:
    for line in file:
        try:
            X.append(line.split(",")[0][2:])
            Y.append(line.split(",")[1][3:])
        except IndexError:
            print(line, "never mind")
print("\n")

X = remove_from_list(X, "p=0\n")
X = remove_from_list(X, "p=1\n")
X = remove_from_list(X, "p=0")
X = remove_from_list(X, "p=1")
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
print(ntmp, "\n")

Xavr = []
Xavr.append(sum(X[deletenum:tmp[0] - deletenum]) / ntmp[0])
Yavr = []
Yavr.append(sum(Y[deletenum:tmp[0] - deletenum]) / ntmp[0])
for i in range(1, len(tmp)):
    Xavr.append(sum(X[tmp[i - 1] + deletenum:tmp[i] - deletenum]) / ntmp[i])
    Yavr.append(sum(Y[tmp[i - 1] + deletenum:tmp[i] - deletenum]) / ntmp[i])

#print("X average: ", Xavr)
#print("Y average: ", Yavr)

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

XD = [51475, 101475, 151475, 51475, 101475, 151475, 51475, 101475, 151475, 51475, 101475, 151475, 51475, 101475, 151475, 5000, 5000, 5000, 5000, 197950, 197950, 197950, 197950]
YD = [85300, 85300, 85300, 135300, 135300, 135300, 185300, 185300, 185300, 5000, 5000, 5000, 265600, 265600, 265600, 60300, 110300, 160300, 210300, 60300, 110300, 160300, 210300]

D = []
for i in range(len(Xavr)):
    D.append(math.sqrt(((Xavr[4] - Xavr[i])**2)+(Yavr[4] - Yavr[i])**2))
D = [x*10 for x in D]
#print(D, "\n")

D0 = []
for i in range(len(XD)):
    D0.append(math.sqrt(((XD[4] - XD[i])**2)+(YD[4] - YD[i])**2))
#print(D0, "\n")

DD = []
for i in range(len(D0)):
    DD.append(D0[i]-D[i])
print("Coordinate deviation:", "\n", DD, "\n")
