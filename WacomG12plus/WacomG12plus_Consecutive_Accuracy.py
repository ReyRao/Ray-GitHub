#   2018 / 11 / 12
#   to calculate WacomG12+ consecutive accuracy
#   data structure: WacomG12+
#   Python3
#   Ray
#   Version: Ver.1
#
##################################################

import os,sys
import numpy as np
import math

path = "C:\\Users\\user\\Desktop\\Ray\\WacomG12plus\\Linearity\\Raw_data"

files = os.listdir(path)
print(files)

filename = input("file: ")

def remove_something(mylist, obj):
    return[x for x in mylist if x != obj]

def average(mylist):
    return[sum(mylist) / len(mylist)]

def intlist(mylist):
    return[int(x) for x in mylist]

def deviation(Xarray, Xavr):
    return[math.sqrt((sum((Xarray - Xavr) ** 2)) / len(Xarray))]

def round_2decimal(value):
    return[((value * 100) + 0.5) / 100]

with open(path + "\\" + filename, "r") as f:
    f = f.readlines()
    f = remove_something(f, "tip=1\n")
    f = [x.split() for x in f]

index = []
cnt = 0
cntnum = 0
cntlist = []
cntnumlist = []
x = []
y = []
xavr = 0
yavr = 0
j = 0
X = []
Y = []
for i in range(len(f)):
    if f[i][0] != "tip=0":
        #print(f[i][0][2:-1], f[i][1][2:-1])
        x.append(f[i][0][2:-1])
        y.append(f[i][1][2:-1])
        cnt += 1
        cntnum += 1
    elif f[i][0] == "tip=0":
        j += 1
        x = intlist(x)
        y = intlist(y)
        cntlist.append(cnt)
        cntnumlist.append(cntnum)
        xavr = average(x)
        yavr = average(y)
        X.append(xavr[0])
        Y.append(yavr[0])
        #xavr = round_2decimal(xavr)
        #yavr = round_2decimal(yavr)
        print(j, "time(s) (X, Y): ", round(xavr[0] * 10, 2), round(yavr[0] * 10, 2))
        cntnum = 0
        x = []
        y = []
        xavr = 0
        yavr = 0
Xavr = 0
Yavr = 0
Xavr = average(X)
Yavr = average(Y)
print("average (X, Y): ", round(Xavr[0] * 10, 2), round(Yavr[0] * 10, 2))
X = np.asarray(X)
Y = np.asarray(Y)

Xdev = 0
Ydev = 0
Xdev = deviation(X, Xavr)
Ydev = deviation(Y, Yavr)
print("one standard deviation (X, Y): ", round(Xdev[0] * 10, 2), round(Ydev[0] * 10, 2))
