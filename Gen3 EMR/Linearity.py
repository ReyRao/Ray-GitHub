#!/usr/bin/Python -tt
#-*- encode:utf-8 -*-
#to analyse linearity
#Ray

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import time

class Coordinate():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.delete_num = 10

    def delete_n(self, delete_num):
        self.delete_num = delete_num
        self.delete_num = int(self.delete_num)

    def row_sep(self):
        x_data_array = []
        y_data_array = []
        index_row = []
        th = 500
        count = 0
        row = [self.x, self.y]
        index_row.append(0)
        for index in range(len(self.x)-1):
            if abs(self.x[index+1] - self.xf[index]) > th or abs(self.y[index+1] - self.y[index]) > th:
                index_row.append(index+1)
        for j in index_row[1:]:
            if self.delete_num >= j:
                switch = False
                print("Data isn't enough! OR Delete too many ponts!")
                raise TypeError("Data isn't enough! OR Delete too many ponts!")
            else:
                switch = True
        if switch == True:
            for k in row:
                for i in range(1, len(index_row)):
                    if count == 0:
                        x_data_array.append(k[index_row[i-1] + self.delete_num : index_row[i] - self.delete_num])
                    else:
                        y_data_array.append(k[index_row[i-1] + self.delete_num : index_row[i] - self.delete_num])
                if self.delete_num != 0:
                    if count == 0:
                        x_data_array.append(k[index_row[-1] + self.delete_num : -self.delete_num])
                    else:
                        y_data_array.append(k[index_row[-1] + self.delete_num : -self.delete_num])
                elif self.delete_num == 0:
                    if count == 0:
                        x_data_array.append(k[index_row[-1]:])
                    else:
                        y_data_array.append(k[index_row[-1]:])
                count += 1
            x_data_array = np.asarray(x_data_array)
            y_data_array = np.asarray(y_data_array)
            return x_data_array, y_data_array

    def np_linearity(self, x_data_array, y_data_array):
        y_pre = []
        for i in range(len(x_data_array)):
            print(x_data_array[i])
            fit = np.polyfit(x_data_array[i], y_data_array[i], 1, full=True)[0]
            formula = np.poly1d(fit)
            y_pre.append(formula(x_data_array[i]))
            a = fit[0]
            b = fit[1]
            d0 = abs(y_data_array[i] - a * x_data_array[i] - b) / (1 + a ** 2) ** (.5)
            ad = sum(d0) / len(x_data_array[i])
            sd = (sum((d0 - ad) ** 2) / len(x_data_array[i])) **(.5)
            (_, j) = max((v, j) for j, v in enumerate(d0))
            print(f"Line {i+1}:")
            print(f"Max Deviation at (x, y): ({x_data_array[i][j]}, {y_data_array[i][j]})")
            print(f"Average Deviation(micrometer): {ad * 10}\n3*Standard Deviation(micrometer): {sd * 30}")
            print("Max deviation(in micrometer): ", max(d0)*10, "\n")
        return y_pre

def main():
    emr_path = r"C:\Users\party\Desktop\Works\Gen.3\Common\Test data"
    files = os.listdir(emr_path)
    print(files)
    emr_data = pd.read_excel(os.path.join(emr_path, files[0]), header=None)
    emr = Coordinate(emr_data[1].values, emr_data[3].values)
    emr.delete_n(10)
    x, y = emr.row_sep()
    emr.np_linearity(x, y)


if __name__ == "__main__":
    main()