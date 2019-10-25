
# !usr/bin/python3
# -*- coding: utf-8 -*-
# to extract EMR Coil Noise data

import sys, os

import pandas as pd
import numpy as np
import csv

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        self.path = None
        self.spath = r'./data.csv'
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(460, 140)
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
        self.extractPushButton = QtWidgets.QPushButton(Form)
        self.extractPushButton.setObjectName("extractPushButton")
        self.verticalLayout.addWidget(self.extractPushButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "EMR Coil Noise Extractor"))
        self.loadDataPushButton.setText(_translate("Form", "Load Data"))
        self.extractPushButton.setText(_translate("Form", "Extract"))
        self.loadDataPushButton.clicked.connect(self.openFileNameDialog)
        self.extractPushButton.clicked.connect(self.extract)

    def openFileNameDialog(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(
                                                            parent=self,
                                                            caption='Select Folder Directory')
        if path:
            self.path = path
        else:
            QtWidgets.QMessageBox.warning(self, "wrong path!", "Choose path first!!!!!!!")
            
    def extract(self):
        with open('data.csv', 'w') as f:
            f.close()
        files = os.listdir(self.path)
        files_list = []
        filename_list = []
        data_list = []
        for i in files:
            if ".csv" in i:
                files_list.append(i)

        for file_name in files_list:
            path = os.path.join(self.path, file_name)
            print(path)
            filename_list.append(file_name[12:-17])

            with open(path, 'r', encoding='utf-8') as file:
                content = file.readlines()
                for i in range(len(content)):
                    content[i] = content[i].split(',')
                    content[i] = content[i][:58]

                df = pd.DataFrame(np.array(content[11:]))
                df.iloc[:, :58] = df.iloc[:, :58].astype('int')
                # print(df.iloc[:, :58].dtypes)
                # print(df.iloc[:, :58].max())
                data = list(df.iloc[:, :58].max())
                data_list.append(data)

                print(file_name[12:-17])
                with open('data.csv', 'a', newline='') as datafile:
                    writer = csv.writer(datafile)
                    writer.writerows([[file_name[12:-17]]])
                    writer.writerows([data])
        QtWidgets.QMessageBox.about(self, 'Finished', 'Finished')


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()