# -*- coding: utf-8 -*-
# Disqus: Rey
# to extract a certain segment of line and then calculate the linearity

import sys
import numpy as np

from PyQt5 import QtCore, QtWidgets


class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.x_orginal = []
        self.y_orginal = []

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 200)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.editXBottom = QtWidgets.QLineEdit(Form)
        self.editXBottom.setAlignment(QtCore.Qt.AlignCenter)
        self.editXBottom.setObjectName("editXBottom")
        self.verticalLayout_2.addWidget(self.editXBottom)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.editXCeiling = QtWidgets.QLineEdit(Form)
        self.editXCeiling.setAlignment(QtCore.Qt.AlignCenter)
        self.editXCeiling.setObjectName("editXCeiling")
        self.verticalLayout_3.addWidget(self.editXCeiling)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.editYBottom = QtWidgets.QLineEdit(Form)
        self.editYBottom.setAlignment(QtCore.Qt.AlignCenter)
        self.editYBottom.setObjectName("editYBottom")
        self.verticalLayout_4.addWidget(self.editYBottom)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.editYCeiling = QtWidgets.QLineEdit(Form)
        self.editYCeiling.setAlignment(QtCore.Qt.AlignCenter)
        self.editYCeiling.setObjectName("editYCeiling")
        self.verticalLayout_5.addWidget(self.editYCeiling)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.pbtnLinearity = QtWidgets.QPushButton(Form)
        self.pbtnLinearity.setObjectName("pbtnLinearity")
        self.verticalLayout.addWidget(self.pbtnLinearity)
        self.editLinearityShow = QtWidgets.QLineEdit(Form)
        self.editLinearityShow.setAlignment(QtCore.Qt.AlignCenter)
        self.editLinearityShow.setObjectName("editLinearityShow")
        self.verticalLayout.addWidget(self.editLinearityShow)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.editLinearityShow.setReadOnly(True)
        self.openFileNameDialog()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Linearity Calculator"))
        self.label.setText(_translate("Form", "X Bottom Limit"))
        self.label_2.setText(_translate("Form", "X Ceiling Limit"))
        self.label_5.setText(_translate("Form", "OR"))
        self.label_3.setText(_translate("Form", "Y Bottom Limit"))
        self.label_4.setText(_translate("Form", "Y Ceiling Limit"))
        self.pbtnLinearity.setText(_translate("Form", "Calculate Linearity (sigma)"))
        
        self.pbtnLinearity.clicked.connect(self.calculate_)
        
    def length_test(self, data, threshold):
        if len(data) <= int(threshold):
            ok = False
            self.editLinearityShow.setText('')
            QtWidgets.QMessageBox.warning(
                self, "Warning!" , f"Lack of data! (data length: {len(data)})")
        else:
            ok = True

        return ok, data

    def compareBottomCeiling(self, bottom, ceiling):
        if bottom >= ceiling:
            switch = False
            self.editLinearityShow.setText('')
            QtWidgets.QMessageBox.warning(self, 'Wrong order', 'ceiling should be larger than bottom!!!!!')
        else:
            switch = True

        return switch

    def setXY(self):
        self.x_orginal = np.asarray(self.x_orginal)
        self.y_orginal = np.asarray(self.y_orginal)

        if self.editYBottom.text() == '':
            self.y_bottom = min(self.y_orginal)
        else:
            self.y_bottom = int(self.editYBottom.text())

        if self.editYCeiling.text() == '':
            self.y_ceiling = max(self.y_orginal)
        else:
            self.y_ceiling = int(self.editYCeiling.text())

        if self.editXBottom.text() == '':
            self.x_bottom = min(self.x_orginal)
        else:
            self.x_bottom = int(self.editXBottom.text())

        if self.editXCeiling.text() == '':
            self.x_ceiling = max(self.x_orginal)
        else:
            self.x_ceiling = int(self.editXCeiling.text())

    def linearity_(self, data, bottom, ceiling):
        x = []
        y = []
        min_index = []
        max_index = []
        index_list = []

        ok = self.compareBottomCeiling(bottom, ceiling)
        if ok:
            for index, value in enumerate(data):
                if ceiling >= value >= bottom:
                    index_list.append(index)

            ok, _ = self.length_test(index_list, 10)
            if ok:
                # print(index_array)
                min_index = index_list[0]
                max_index = index_list[-1]

                y = self.y_orginal[min_index : max_index]
                x = self.x_orginal[min_index : max_index]

                x = np.asarray(x)
                y = np.asarray(y)
                print(f'x: {len(x)}, x[0]: {x[0]}, x[-1]: {x[-1]}')
                print(f'y: {len(y)}, y[0]: {y[0]}, y[-1]: {y[-1]}')

                fit = np.polyfit(x, y, 1, full=True)[0]
                a = fit[0]
                b = fit[1]
                d0 = abs(y - a * x - b) / (1 + a ** 2) ** (.5)
                ad = sum(d0) / len(x)
                sd = (sum((d0 - ad) ** 2) / len(x)) **(.5)

                self.editLinearityShow.setText(str(sd))

    def inverse_(self, bottom, ceiling):
        if bottom > ceiling:
            self.y_orginal = self.y_orginal[::-1]
            self.x_orginal = self.x_orginal[::-1]

    def openFileNameDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.path, _ = QtWidgets.QFileDialog.getOpenFileName(  self,
                                                    "QFileDialog.getOpenFileName()",
                                                    "",
                                                    "All Files (*);;Python Files (*.py)",
                                                    options = options)
        # self.path = str(fileName)
        print(self.path)


    def calculate_(self):
        self.x_orginal = []
        self.y_orginal = []
        # path = r'./MD1_line2.txt'
        
        print(self.path)

        with open(self.path, 'r', newline='', encoding='utf-8') as file:
            line = file.readlines()
            line = [x.split() for x in line]
            for i in range(len(line)):
                self.x_orginal.append(int(line[i][3].split(',')[5]))
                self.y_orginal.append(int(line[i][3].split(',')[6]))
        # print(f'self.x_orginal: {self.x_orginal[0]}, {self.x_orginal[-1]}, len: {len(self.x_orginal)}')
        # print(f'self.y_orginal: {self.y_orginal[0]}, {self.y_orginal[-1]}, len: {len(self.y_orginal)}')

        self.setXY()

        if self.editXBottom.text() == '' and self.editXCeiling.text() == '':
            self.inverse_(self.y_bottom, self.y_ceiling)
            self.linearity_(self.y_orginal, self.y_bottom, self.y_ceiling)

        elif self.editYBottom.text() == '' and self.editYCeiling.text() == '':
            self.inverse_(self.x_bottom, self.x_ceiling)
            self.linearity_(self.x_orginal, self.x_bottom, self.x_ceiling)

        else:
            self.editLinearityShow.setText("")
            QtWidgets.QMessageBox.about(self, 'Decision!', "Just choose one! Don't be so greedy!")


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()