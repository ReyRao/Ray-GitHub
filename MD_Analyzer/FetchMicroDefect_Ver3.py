# !usr/bin/Python3
# Purpose         : To Fetch MicrDefect data
# Programmer      : Rey
# Version         : Ver.3
#########################################
import os, sys
from numpy import *
from scipy import stats

path = "C:\\Users\\party\\Desktop\\Ray\\Data_analysis\\FAIL"
spath = "C:\\Users\\party\\Desktop\\Ray\\Data_analysis"
files = os.listdir(path)


xth = input("Please enter your X condition(%): ")
yth = input("Please enter your Y condition(%): ")

Xthreshold = int(xth)
Ythreshold = int(yth)

with open(spath + "\\XTest.txt", "a") as fx, open(spath + "\\YTest.txt", "a") as fy:
    fx.write("\n")
    fx.write("\n")
    fx.write("X Line,X0-X1,X1-X2,X2-X3,X3-X4,X4-X5,X5-X6,X6-X7,X7-X8,X8-X9,X9-X10,X10-X11,X11-X12,X12-X13,X13-X14,X14-X15,X15-X16,X16-X17,X17-X18,X18-X19,X19-X20,X20-X21,X21-X22,X22-X23,X23-X24,X24-X25,X25-X26,X26-X27,X27-X28,X28-X29,X29-X30,X30-X31,X31-X32,X32-X33,X33-X34,X34-X35,X35-X36,X36-X37")
#    fx.write("\n")
    fy.write("\n")
    fy.write("\n")
    fy.write("Y Line,Y0-Y1,Y1-Y2,Y2-Y3,Y3-Y4,Y4-Y5,Y5-Y6,Y6-Y7,Y7-Y8,Y8-Y9,Y9-Y10,Y10-Y11,Y11-Y12,Y12-Y13,Y13-Y14,Y14-Y15,Y15-Y16,Y16-Y17,Y17-Y18,Y18-Y19,Y19-Y20,Y20-Y21,Y21-Y22,Y22-Y23,Y23-Y24,Y24-Y25,Y25-Y26,Y26-Y27,Y27-Y28,Y28-Y29,Y29-Y30,Y30-Y31,Y31-Y32,Y32-Y33,Y33-Y34,Y34-Y35,Y35-Y36,Y36-Y37,Y37-Y38,Y38-Y39,Y39-Y40,Y40-Y41,Y41-Y42,Y42-Y43,Y43-Y44,Y44-Y45,Y45-Y46,Y46-Y47,Y47-Y48,Y48-Y49,Y49-Y50")
#    fy.write("\n")

s = []
for file in files:
    try:
        if not os.path.isdir(file):
            X_diff = []
            Y_diff = []
            Xline = 0
            Yline = 0
            fp = path + "\\" + file
            with open(fp, "r") as f:
                f = iter(f)
            #Find the index of differential
                for i, line in enumerate(f):
                    if "36) MicroDefect" in line:
                        Xline = i + 12
                        Yline = i + 16
            #Save the target line
            f = open(fp, "r")
            lines = f.readlines()
            X_diff.append(lines[Xline])
            Y_diff.append(lines[Yline])

            X_diff = [x.strip() for x in X_diff]
            Y_diff = [y.strip() for y in Y_diff]
            # print(X_diff)

            X = "".join(str(x) for x in X_diff)
            Y = "".join(str(y) for y in Y_diff)
            f.close()

            with open(spath + "\\XTest.txt", "a") as fx, open(spath + "\\YTest.txt", "a") as fy:

                # fx.write("\n")
                X = X.replace("%", "")
                X = X.replace("Diff", "")
                X = X.replace(",", " ")
                x_float = [float(x) for x in X.split()]
                # print(x_float)
                xdiff = []
                
                for i in x_float:
                    if i <= Xthreshold:
                        i = " ,"
                    elif i > Xthreshold:
                        i = str(i) + ","
                    xdiff.append(i)
                xdiff = "".join(str(x) for x in xdiff)
                
                fx.write(file + ",")
                fx.write(xdiff)

                fy.write("\n")
                Y = Y.replace("%", "")
                Y = Y.replace("Diff", "")
                Y = Y.replace(",", " ")
                y_float = [float(y) for y in Y.split()]
                ydiff = []
                
                for i in y_float:
                    if i <= Ythreshold:
                        i = " ,"
                    elif i > Ythreshold:
                        i = str(i) + ","
                    ydiff.append(i)
                ydiff = "".join(str(y) for y in ydiff)
                
                fy.write(file + ",")
                fy.write(ydiff)
                
            os.rename(os.path.join(path, file), os.path.join(path, str(max(y_float)) + "____" + file))

    except (IndexError, PermissionError):
        print(file, "can't not read")
        print(file, "is opening now!, Please close it and clean the saving text!")

f.close()
fx.close()
fy.close()

