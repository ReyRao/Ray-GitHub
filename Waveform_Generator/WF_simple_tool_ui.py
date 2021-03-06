# -*- coding: utf-8 -*-

import sys

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

    def draw(self):
        df = pd.read_excel(self.path, header=None, encoding='utf-8')
        
        ax = []
        for i in range(len(df.columns)):
            ax.append(f'ax{i}')

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



def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()