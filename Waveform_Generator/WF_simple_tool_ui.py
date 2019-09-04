# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WF_simple_toole.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

import sys

import pandas as pd
import matplotlib.pyplot as plt

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
        ax = []
        for i in range(len(df.columns)):
            ax.append(f'ax{i}')

        _, ax = plt.subplots(len(df.columns), sharex=True, sharey=True, gridspec_kw={'hspace': 0}, figsize=(15, 6))

        for i in range(len(df.columns)):
            x = range(len(df.iloc[2:, i]))
            ax[i].plot(x, df.iloc[2:, i], label=f'{df.iloc[0, i]}->{df.iloc[1, i]}')
            ax[i].legend(loc=0)
            ax[i].set_xticks(x)

        ax[0].set_title("Visualised WF")
        plt.tight_layout()
        plt.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()