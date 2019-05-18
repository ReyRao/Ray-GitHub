#!usr/bin/python3

# d = [0,1,2,3,4,5,6,7,8,9]
# print(d[:4])


# form = pd.DataFrame(
#     {"a": np.random.randint(1, 10, 5),
#     "b": np.random.randint(10, 20, 5),
#     "c": np.random.randint(20, 30, 5)})

# print(form)
# print("seperate here".center(100, "-"))
# print("loc: ")
# print(form.loc[3,["b", "c"]])
# print("seperate here".center(100, "-"))
# print("iloc: ")
# print(form.iloc[:4, 1:])
# print("seperate here".center(100, "-"))
# print("ix: ")
# print(form.ix[])
# print("seperate here".center(100, "-"))

# list = ['EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3']
# for i, source in enumerate(list):
#     # 做 subplot
#     print(i, source)

# for i in list:
#     print(i)

# import  time
# from progressbar import *

# total = 1000

# def dosomework():
#     time.sleep(0.01)

# widgets = ['Progress: ',Percentage(), ' ', Bar('#'),' ', Timer(),
#         ' ', ETA(), ' ', FileTransferSpeed()]
# pbar = ProgressBar(widgets=widgets, maxval=10*total).start()
# for i in range(total):
#     # do something
        
#     pbar.update(10 * i + 1)
#     dosomework()
# pbar.finish()

# dic = {"a":[1], "b":[2], "c":[3], "d":[4], "e":[5]}
# df = pd.DataFrame(dic)
# print(df, "\n")
# df1 = df[["b"]].copy()
# print(type(df1))
# df2 = df["b"].copy()
# print(type(df2))
# df3 = df.copy()
# print(type(df3))


# def add(x, y):
#     z = x + y
#     print(x, y)
#     return z

# if __name__ == "__main__":
#     add(1, 2)
#     print("seperate here".center(50, "-"))
#     print(add(1, 2))
#     time.sleep(3)

# lang = "python"
# print(lang[::-1])


##########################################################3

# import numpy as np
# import scipy.linalg
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt

# # some 3-dim points
# mean = np.array([0.0,0.0,0.0])
# cov = np.array([[1.0,-0.5,0.8], [-0.5,1.1,0.0], [0.8,0.0,1.0]])
# data = np.random.multivariate_normal(mean, cov, 1)

# print("data: ", "\n", data, "\n", "\n")
# # regular grid covering the domain of the data
# X,Y = np.meshgrid(np.arange(-3.0, 3.0, 0.5), np.arange(-3.0, 3.0, 0.5))

# print(X, "\n", "\n", Y)

# XX = X.flatten()
# YY = Y.flatten()
# print(XX)

# order = 2    # 1: linear, 2: quadratic
# if order == 1:
#     # best-fit linear plane
#     A = np.c_[data[:,0], data[:,1], np.ones(data.shape[0])]
#     C,_,_,_ = scipy.linalg.lstsq(A, data[:,2])    # coefficients
    
#     # print(C)

#     # evaluate it on grid
#     Z = C[0]*X + C[1]*Y + C[2]
    
#     # or expressed using matrix/vector product
#     #Z = np.dot(np.c_[XX, YY, np.ones(XX.shape)], C).reshape(X.shape)

# elif order == 2:
#     # best-fit quadratic curve
#     A = np.c_[np.ones(data.shape[0]), data[:,:2], np.prod(data[:,:2], axis=1), data[:,:2]**2]
#     C,_,_,_ = scipy.linalg.lstsq(A, data[:,2])

#     print(A, "\n", "\n", C)

#     # evaluate it on a grid
#     Z = np.dot(np.c_[np.ones(XX.shape), XX, YY, XX*YY, XX**2, YY**2], C).reshape(X.shape)

# # plot points and fitted surface
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, alpha=0.2)
# ax.scatter(data[:,0], data[:,1], data[:,2], c='r', s=50)
# plt.xlabel('X')
# plt.ylabel('Y')
# ax.set_zlabel('Z')
# ax.axis('equal')
# ax.axis('tight')
# plt.show()

##########################################################
# import numpy as np

# x0 = np.array([[1, 2, 3], [4, 5, 6]])
# y0 = np.array([1, 0 ,1])
# z0 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]])
# listy = [1, 2, 3]

# print(np.dot(x0, y0))

# X,Y = np.meshgrid(np.arange(1, 38.5, 0.5), np.arange(1, 51.5, 0.5))
# print(X.shape)


##############################################################################
# import seaborn as sns
# import matplotlib.pyplot as plt

# num = 1000
# x = np.linspace(0, num, num)
# mean = 0
# std = 1
# y = np.random.normal(mean, std, num)
# # sns.regplot(x, y)
# plt.scatter(x, y)
# sns.regplot(x, y)
# plt.show()

################################################3
# import numpy as np
# import matplotlib.pyplot as plt

# np.random.seed(5)

# def Mean(list):
#     return round(sum(list) / len(list), 2)

# def r_square(data):
#     order = 2
#     x = np.linspace(1, len(data), len(data)) 
#     y = data
#     fit = np.polyfit(x, y, order, full=True)[0]
#     residuals = np.polyfit(x, y, order, full=True)[1]
#     formula = np.poly1d(fit)
#     y_bar = Mean(data)
#     y_hat = formula(x)
#     SSR = sum((y_hat - y_bar)**2)
#     SSE = sum((y - y_hat)**2)
#     SSTO = sum((y - y_bar)**2)
#     return SSR/SSTO


# data1 = np.random.normal(5, 0.05, 300)
# data2 = np.random.normal(10, 0.3, 300)
# x = np.linspace(1, len(data1), len(data1))
# y1 = data1
# y2 = data2

# fit1 = np.polyfit(x, y1, 2, full=True)[0]
# residuals = np.polyfit(x, y1, 2, full=True)[1]
# formula1 = np.poly1d(fit1)

# fit2 = np.polyfit(x, y2, 2, full=True)[0]
# residuals = np.polyfit(x, y2, 2, full=True)[1]
# formula2 = np.poly1d(fit2)

# print(r_square(y1), r_square(y2))

# plt.scatter(x, y1, s=2)
# plt.scatter(x, y2, s=2)
# plt.plot(x, formula1(x))
# plt.plot(x, formula2(x))
# plt.show()

###############################################################

# import numpy as np
# import pandas as pd
# b = []
# def summ(a):
#     b.append(sum(a))
#     # print(b)
#     return None
# a = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
# b = np.array([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]])
# a_df = pd.DataFrame(a)
# b_df = pd.DataFrame(b)
# z = np.zeros([2, 6])
# z = pd.DataFrame(z)


# print()


################################
# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     'Animal' : ['dog', 'cat', 'cat', 'cat'],
#     'Max Speed' : [380., 370., 24., 26.],
#     'Min Speed' : [10, 10, 30, 40]
#     })    
# count_df = df.groupby()
# import copy

# a = [[0, 0], 1, 2, 3]
# b = a
# c = copy.deepcopy(a)
# b[0][0] = 9

# print(b, "\n", c, "\n", a)

# from datetime import datetime
# import time


# print(datetime.now(), "\n", time.time())

# a = [0,1,2,3,4,1]
# b = [[0,1,2,3,4,1], 0]

# print(len(a), "\n", len(b))

# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.preprocessing import LabelEncoder

# MMscaler = MinMaxScaler()
# LEncodor = LabelEncoder()

# dfTest = pd.DataFrame({
#     'A':[14.00,90.20,90.95,96.27,91.21],
#     'B':[103.02,107.26,110.35,114.23,114.68],
#     'C':['big','small','big','small','small']
#     })

# dfTest["C"] = LEncodor.fit_transform(dfTest["C"])

# dfTest_MMscaler = MMscaler.fit_transform(dfTest)
# dfTest_MMscaler_A = MMscaler.fit_transform(dfTest["A"].values.reshape(-1,1))

# print(dfTest_MMscaler, "\n", dfTest_MMscaler_A)

#############################################################################
# import pandas as pd
# import numpy as np

# arr = []
# for i in range(10):
#     arr.append([])
#     for j in range(5):
#         arr[i].append(i*j)
# print(len(arr))
##############################################################################

# from progressbar import *
# import numpy as np

# def dosomework():
#     time.sleep(0.01)

# widgets = ['Progress: ',Percentage(), ' ', Bar('#'),' ', Timer(),
#         ' ', ETA(), ' ', FileTransferSpeed()]
# pbar = ProgressBar(widgets=widgets, maxval=10*99).start()


# for i in range(99):
#     x = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#     y = np.array([[1, 1, 1, 1, 1], [2, 2, 2, 2, 2]])
#     z = x*i+y**2+x**y
#     pbar.update(10 * i+1)
#     dosomework()
# pbar.finish()

# print(z)

##################################################################

# columns_ = ["Y" + str(x) for x in range(51)]
# index_ = ["X" + str(x) for x in range(38)]
# print(columns_, index_)


#######################################################################
# import numpy as np

# def mean_(list):
#     return round(sum(list) / len(list), 2)

# list = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# result = list - mean_(list)
# print(mean_(list), result)

######################################################################
# import pandas as pd
# import numpy as np

# def title(str):
#     return pd.DataFrame(np.array(["whatever"]), columns=[" "], index=[str])

# print(title("Cm"))

##########################################################################
# class Coordinate():
#     def __init__(self, x):
#         self.x = x

#     def x_plus_times100(self, x2):
#         self.x2 = x2
#         return (self.x + self.x2) * 100

#     def x_squared(self):
#         self.x2 = self.x ** 2
#         return self.x2

# def main():
#     x = Coordinate(2)
#     y = Coordinate(5)
#     x.x_squared()
    
#     print(x.x_plus_times100(y.x_squared()))
#     # x.x_squared()
#     print(x.x2)
#     print(y.x2)
#     print(x.x_plus_times100(9))
#     print(x.x2)
#     print(y.x2)

# if __name__ == "__main__":
#     main()

##################################################################

# import numpy as np
# from sklearn import metrics

# x = np.array([1, 1, 1, 1, 0, 0, 0, 0, 0, 0])
# y = np.array([1, 1, 0, 0, 1, 1, 1, 1, 1, 1])

# acc = metrics.accuracy_score(x, y)
# print(acc)

############################################

# from sklearn.model_selection import KFold
# import numpy as np
# X = np.array([[[1, 2], [3, 4]], [[1, 2], [3, 4]]])
# print(X.shape)
# y = np.array([1, 2, 3, 4])
# kf = KFold(n_splits=2)
# for train_index, test_index in kf.split(X):
#     print("TRAIN:", train_index, "TEST:", test_index)

##########################################################

# import numpy as np

# x= np.arange(1, 15)
# print(x[0])

# y = enumerate(x)
# print(y)


###########################################################
# import numpy as np
# import matplotlib.pyplot as plt

# from sklearn.cluster import KMeans
# from sklearn.datasets import make_blobs

# plt.figure(figsize=(12, 12))

# n_samples = 1500
# random_state = 170
# X, y = make_blobs(n_samples=n_samples, n_features=2, random_state=random_state)

# # Incorrect number of clusters
# y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X)

# plt.subplot(221)
# plt.scatter(X[:, 1], X[:, 0], c=y_pred)
# plt.title("Incorrect Number of Blobs")

# # Anisotropicly distributed data
# transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
# X_aniso = np.dot(X, transformation)
# y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X_aniso)

# plt.subplot(222)
# plt.scatter(X_aniso[:, 0], X_aniso[:, 1], c=y_pred)
# plt.title("Anisotropicly Distributed Blobs")

# # Different variance
# X_varied, y_varied = make_blobs(n_samples=n_samples,
#                                 cluster_std=[1.0, 2.5, 0.5],
#                                 random_state=random_state)
# y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X_varied)

# plt.subplot(223)
# plt.scatter(X_varied[:, 0], X_varied[:, 1], c=y_pred)
# plt.title("Unequal Variance")

# # Unevenly sized blobs
# X_filtered = np.vstack((X[y == 0][:500], X[y == 1][:100], X[y == 2][:10]))
# y_pred = KMeans(n_clusters=3,
#                 random_state=random_state).fit_predict(X_filtered)

# plt.subplot(224)
# plt.scatter(X_filtered[:, 0], X_filtered[:, 1], c=y_pred)
# plt.title("Unevenly Sized Blobs")

# plt.show()

# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np


# fig = plt.figure()
# ax = Axes3D(fig)
# X = np.arange(-4, 4, 0.25)
# Y = np.arange(-4, 4, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)

# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')
# ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.cm.hot)
# ax.set_zlim(-2, 2)
# plt.show()


# class CapStr(str):
#     def __init__(self,string):
#         self.string = string
#         self.string = self.string.upper()

# a = CapStr("I love China!")
# print(a)


# class CapStr(str):
#     def __new__(cls,string):
#         string = string.upper()
#         return super().__new__(cls,string)

# b = CapStr("I love China!")
# print(b)

# print(
#     set('abc'), '\n',
#     {'a', 'b', 'c'}
# )
# x = 3
# print(id(x))
# # x = 'wat'
# # print(id(x))

# sF = [0.8, 0.9, 1.0]
# mN = [1, 2, 3]
# # for x, y in [(x, y) for x in sF for y in mN]:
#     # print(x, y)
# # print(sF, mN)
# print(sF*mN)
# # print('\n')
# import numpy as np
# sFa = np.asarray(sF)
# mNa = np.asarray(mN)
# for x, y in [(x, y) for x in sFa for y in mNa]:
    # print(x, y)
# print(sFa, mNa)
#########################################################
# import numpy as np
# print([10]*5)


# s = 'testing'
# l = len(s)
# try:
#     position = l/2
#     if l%2 != 0:
#         print(s[int(position-0.5)])
#     else:
#         print(s[int(position-1):int(position+1)])
# except:
#     print('empty string')

# n = 1810
# result = 0
# if n//10 == 0:
#     print(n)
# while n//10 != 0:
#     result += n%10
#     n = n//10
#     print(result)
#     if n//10  == 0:
#         result += n%10
#         print(result)

# def digital_root(n):
#     for i in str(n):
#         print(i)

# print(digital_root(199))

# import re
# test_string = 'aabb abb aab abbb'
# pattern = 'a*b'
# ans=re.findall(pattern,test_string)
# print(ans)

##########################################3
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(0, 50, 0.1)
# x = np.linspace(0, 49, 490)
# print(x[:10])
FCT = 23
HCT = 11
upper1 = 23000 * 1.05
upper2 = 23000 * 1.043
y1 = upper1 * x / (1.3 + abs(x))
y2 = upper2 * x / (0.75 + abs(x))

plt.plot(x, y1, color='b')
plt.plot(x, y2, color='g')

plt.text(22, upper1-2700, 'FULL(CT=%i, Cm=%i)' %(FCT, y1[FCT*10]), color='r')
plt.plot(x[FCT*10], y1[FCT*10], 'r*', markersize=12)
plt.text(8, upper1-4500, 'Half(CT=%i, Cm=%i)' %(HCT, y1[HCT*10]), color='b')
plt.plot(x[HCT*10], y1[HCT*10], 'r*',color='b', markersize=12)

plt.text(22, upper2-200, 'FULL(CT=%i, Cm=%i)' %(FCT, y2[FCT*10]), color='r')
plt.plot(x[FCT*10], y2[FCT*10], 'r*', markersize=12)
plt.text(2, upper2-800, 'Half(CT=%i, Cm=%i)' %(HCT, y2[HCT*10]), color='b')
plt.plot(x[HCT*10], y2[HCT*10], 'r*',color='b', markersize=12)


plt.title('Charging-rate Scheme', size=15)
plt.ylabel('Mutual Capacity (Cm)')
plt.xlabel('Cycle Time (CT)')
plt.tight_layout()
plt.show()
####################################################