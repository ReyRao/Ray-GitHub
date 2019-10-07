# -*- coding: utf-8 -*-

<<<<<<< HEAD
=======
# Form implementation generated from reading ui file 'WF_simple_toole.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

>>>>>>> 0b75f92f364ec0d73eabb1c9fe33c74aefb2edd6
import sys

import pandas as pd
import matplotlib.pyplot as plt
<<<<<<< HEAD
import numpy as np
=======
>>>>>>> 0b75f92f364ec0d73eabb1c9fe33c74aefb2edd6

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.path = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 150)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.loadDataPushButton = QtWidgets.QPushButton(Form)
        self.loadDataPushButton.setObjectName("loadDataPushButton")
        self.verticalLayout.addWidget(self.loadDataPushButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.convertPushButton = QtWidgets.QPushButton(Form)
        self.convertPushButton.setObjectName("convertPushButton")
        self.verticalLayout.addWidget(self.convertPushButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.loadDataPushButton.setText(_translate("Form", "Load Data"))
        self.convertPushButton.setText(_translate("Form", "Convert"))

        self.loadDataPushButton.clicked.connect(self.openFileNameDialog)
        self.convertPushButton.clicked.connect(self.draw)

    def openFileNameDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.path, _ = QtWidgets.QFileDialog.getOpenFileName(  self,
                                                                "Choose a file",
                                                                "",
                                                                "All Files (*);;Excel (*.xls, *.xlsm, *.xlsx)",
                                                                options = options)
<<<<<<< HEAD

    def draw(self):
        df = pd.read_excel(self.path, header=None, encoding='utf-8')
        
=======
        # print(self.path)

    def draw(self):
        df = pd.read_excel(self.path, header=None, encoding='utf-8')
        # plt.figure(figsize=(6, 8))
        # for i in range(len(df.index)):
        #     print(df.iloc[i, 2:])
        
        #     plt.plot(range(len(df.iloc[i, 2:])), df.iloc[i, 2:])
        # plt.plot(range(len(df.iloc[i, 2:])), [0]*len(df.iloc[i, 2:]), '--')
        # plt.ylim(-1.5, 1.5)
        # print(df)
>>>>>>> 0b75f92f364ec0d73eabb1c9fe33c74aefb2edd6
        ax = []
        for i in range(len(df.columns)):
            ax.append(f'ax{i}')

<<<<<<< HEAD
        plt.style.use('seaborn-whitegrid')
        _, ax = plt.subplots(   len(df.columns), sharex=True, sharey=True,
                                gridspec_kw={'hspace': 0}, figsize=(9, 4))
        legend_prperties = {'weight':'bold', 'size':'15', 'style':'italic', 'family':'fantasy'}

        for i in range(len(df.columns)):
            # print(f'round {i}')
            x = range(len(df.index)-2)
            x_mod = np.linspace(x[0], x[-1], 2*len(x)-1)
            n = 0
            for index, value in enumerate(x_mod):
                if value % 1 !=0:
                    x_mod = np.insert(x_mod, index+n, value, axis=0)
                    n += 1

            data = np.asarray(df.iloc[2:, i])
            # print("orginal: ", data)
            data_mod = []
            for j in range(len(data)-1):
                data_mod.append(data[j])
                data_mod.append(data[j])
                data_mod.append(data[j+1])
            data_mod.append(data[-1])

            ax[i].plot( x_mod,
                        [0 for i in range(len(x_mod))],
                        color='grey')
            ax[i].plot( x_mod, 
                        data_mod, 
                        label=f'{df.iloc[0, i]} > {df.iloc[1, i]}', 
                        color="b")
            
            ax[i].legend(loc=0, frameon=False, prop=legend_prperties, shadow=True)
            ax[i].set_xticks(x)
            ax[i].set_yticks([-1, 0, 1])
            ax[i].set_ylim([-1.15, 1.15])

        ax[0].set_title("Visualised WFs")
        plt.tight_layout()
        plt.show()


=======
        _, ax = plt.subplots(len(df.columns), sharex=True, sharey=True, gridspec_kw={'hspace': 0}, figsize=(15, 6))

        for i in range(len(df.columns)):
            x = range(len(df.iloc[2:, i]))
            ax[i].plot(x, df.iloc[2:, i], label=f'{df.iloc[0, i]}->{df.iloc[1, i]}')
            ax[i].legend(loc=0)
            ax[i].set_xticks(x)

        ax[0].set_title("Visualised WF")
        plt.tight_layout()
        plt.show()

>>>>>>> 0b75f92f364ec0d73eabb1c9fe33c74aefb2edd6
def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()