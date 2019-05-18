# to randomly create two Cm rows\
#  and simulate the calculation of TP IC venders 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

def create_row(n=10, full=True, deviation=100, nor=True):
    if full == True:
        if nor == True:
            row = np.abs(np.random.randn(n)) * deviation + 23231
        else:
            row = np.abs(np.random.randn(n)) * deviation + 22858
        return row
    else:
        if nor == True:
            row = np.abs(np.random.randn(n)) * deviation + 22457
        else:
            row = np.abs(np.random.randn(n)) * deviation + 21597
        return row

def atmel_method(row1, row2):
    row1_mean = np.mean(row1)
    row2_mean = np.mean(row2)
    result = (row2_mean - row1_mean) / (row1_mean - 16384)
    print(f'result: {abs(100*result):.2f} %')

def parade_method(row1, row2):
    row1_mean = np.mean(row1)
    row2_mean = np.mean(row2)
    row1_max = max(row1)
    row1_min = min(row1)
    result = (row1_max - row1_min + \
        abs(row1_mean - row2_mean)) / row1_mean
    print(f'result: {abs(100*result):.2f} %')


row1_full_nor = create_row(n=33, full=True)
row1_half_nor = create_row(n=33, full=False)
row1_full_abnor = create_row(n=33, full=True, nor=False)
row1_half_abnor = create_row(n=33, full=False, nor=False)

row2_full_nor = create_row(n=33, full=True)
row2_half_nor = create_row(n=33, full=False)
row2_full_abnor = create_row(n=33, full=True, nor=False)
row2_half_abnor = create_row(n=33, full=False, nor=False)

print('Atmel(HN vs. HN):')
atmel_method(row1_half_nor, row2_half_nor)
print('Atmel(HN vs. HaN):')
atmel_method(row1_half_nor, row2_half_abnor)
print('Parade(FN vs. FN):')
parade_method(row1_full_nor, row2_full_nor)
print('Parade(FN vs. FaN):')
parade_method(row1_full_nor, row2_full_abnor)
# print('Atmel(HaN vs. HaN):')
# atmel_method(row1_half_abnor, row2_half_abnor)
# print('Parade(FaN vs. FaN):')
# parade_method(row1_full_abnor, row2_full_abnor)




#############################################################
# plot the simulation data
plt.figure(figsize=(6, 4))
plt.plot(row1_full_nor, label='full_nor')
plt.plot(row1_half_nor, label='half_nor')
plt.plot(row1_full_abnor, label='full_abnor')
plt.plot(row1_half_abnor, label='half_abnor')
plt.legend()
plt.title("row1")

plt.figure(figsize=(6, 4))
plt.plot(row2_full_nor, label='row2_full_nor')
plt.plot(row2_half_nor, label='row2_half_nor')
plt.plot(row2_full_abnor, label='row2_full_abnor')
plt.plot(row2_half_abnor, label='row2_half_abnor')
plt.legend()
plt.title("row2")

plt.show()