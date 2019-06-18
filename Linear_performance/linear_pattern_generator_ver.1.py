# usr/bin/python
# to create linear performance drawing coordinate

import sys
import numpy as np
import matplotlib.pyplot as plt
import csv
from time import sleep


from PyQt5 import QtCore, QtGui, QtWidgets


class Lpg(QtWidgets.QWidget):
    def __init__(self, width=156200, height=208600, indent=1000, shift=1050, n_line=7):
        # width=156200, height=208600, indent=1000, shift=1050, n_line=7
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.n_line = n_line
        self.shift = shift
        self.indent = indent
        self.height = height
        self.org_height = self.height
        self.height = self.height - 2 * self.indent
        self.width = width
        self.org_width = self.width
        self.width = self.width - 2 * self.indent
        self.orthogonalPath = "./orthogonal.csv"
        self.orthogonal_switch = True
        self.link = None

    def textValue(self, value):
        return self.value

    def exitApp(self):
        exit()

    def getIndent(self):
        num, ok = QtWidgets.QInputDialog.getInt(self, "Indent table", "enter indent value")
        if ok:
            self.indent = num
            self.edit_indent.setText(str(self.indent))
            if self.indent<0:
                QtWidgets.QMessageBox.warning(self, "Warning !", "This value cannot be negtive !")
                self.edit_indent.setText("Error")

    def getShift(self):
        num, ok = QtWidgets.QInputDialog.getInt(self, "Shift table", "enter shift value")
        if ok:
            self.shift = num
            self.edit_shift.setText(str(self.shift))
            if self.shift<=0:
                QtWidgets.QMessageBox.warning(self, "Warning !", "This Value should be positive !")
                self.edit_shift.setText("Error")

    def getNlines(self):
        num, ok = QtWidgets.QInputDialog.getInt(self, "Line's #", "enter lines' #")
        if ok:
            self.n_line = num
            self.edit_n_lines.setText(str(self.n_line))
            if self.n_line<=0:
                QtWidgets.QMessageBox.warning(self, "Warning !", "This Value should be positive !")
                self.edit_n_lines.setText("Error")
            elif self.n_line%2==0:
                QtWidgets.QMessageBox.warning(self, "Warning !", "line's # must be odd")
                self.edit_n_lines.setText("Error")

    def getHeight(self):
        num, ok = QtWidgets.QInputDialog.getInt(self, "Height table", "enter height value")
        if ok:
            self.height = num
            self.edit_height.setText(str(self.height))
            if self.height<=0:
                QtWidgets.QMessageBox.warning(self, "Warning !", "This Value should be positive !")
                self.edit_height.setText("Error")

    def getWidth(self):
        num, ok = QtWidgets.QInputDialog.getInt(self, "Width table", "enter width value")
        if ok:
            self.width = num
            self.edit_width.setText(str(self.width))
            if self.width<=0:
                QtWidgets.QMessageBox.warning(self, "Warning !", "This Value should be positive !")
                self.edit_width.setText("Error")

    def defaultWarining(self):
        # width=156200, height=208600, indent=1000, shift=1050, n_line=7
        if self.org_height==208600:
            QtWidgets.QMessageBox.about(self, "Heads-up!", f"Height is default({208600}).")
        if self.org_width==156200:
            QtWidgets.QMessageBox.about(self, "Heads-up!", f"Width is default({156200}).")
        if self.indent==1000:
            QtWidgets.QMessageBox.about(self, "Heads-up!", f"indent is default({1000}).")
        if self.shift==1050:
            QtWidgets.QMessageBox.about(self, "Heads-up!", f"shift is default({1050}).")
        if self.n_line==11:
            QtWidgets.QMessageBox.about(self, "Heads-up!", f"# of line is default({11}).")

        if self.height|self.width|self.shift|self.n_line<=0 or self.indent<0 or self.n_line%2==0:
            QtWidgets.QMessageBox.warning(self, "Warining !", "!!!!! Values Error !!!!!")
            QtWidgets.QMessageBox.warning(self, "Warining !", "!!!!! Values Error !!!!!")
            QtWidgets.QMessageBox.warning(self, "Warining !", "!!!!! Values Error !!!!!")
            QtWidgets.QMessageBox.warning(self, "Warining !", "It's very important so it pops up three times!!!")
            self.orthogonal_switch = False

    def orthogonalLine(self):
        self.defaultWarining()

        if self.orthogonal_switch == True:
            a = 1
            b = 0
            x = self.width // 2
            y = a * x + b
            y_list_p = []
            y_list_n = []
            
############# for centre
            for i in range(1, self.n_line + 1):
                y_centre_p = y + self.n_line // 2 * self.shift
                y_centre_p = y_centre_p - (i - 1) * self.shift
                y_centre_n = y_centre_p * -1
                y_list_p.append(y_centre_p)
                y_list_n.append(y_centre_n)
            y_list_n = y_list_n[::-1]
            y_list = []
            for i in range(len(y_list_p)):
                y_list.append(y_list_p[i])
                y_list.append(y_list_n[i])
            # print(f"y center list: {y_list}\n")
            # print(f"b: {b}")
            plt.figure(figsize=(6, 8))
            for i in range(0, len(y_list)-1, 2):
                plt.plot([x, -x], [y_list[i], y_list[i+1]], c='black')
                plt.plot([-x, x], [y_list[i], y_list[i+1]], c='black')

            # save data
            with open(self.orthogonalPath, 'a', newline='') as file:
                writer = csv.writer(file)
                # write center
                for i in range(0, 2*self.n_line, 2):
                    writer.writerow([x, y_list[i], 0, 0, 0, 300, -1])
                    sleep(0.01)
                    writer.writerow([x, y_list[i], 4000, 0, 0, 10, -1])
                    sleep(0.01)
                    writer.writerow([-x, y_list[i+1], 4000, 0, 0, 10, -1])
                    sleep(0.01)
                    writer.writerow([-x, y_list[i+1], 0, 0, 0, 300, -1])
                    sleep(0.01)
                for i in range(0, 2*self.n_line, 2):
                    writer.writerow([-x, y_list[i], 0, 0, 0, 300, -1])
                    sleep(0.01)
                    writer.writerow([-x, y_list[i], 4000, 0, 0, 10, -1])
                    sleep(0.01)
                    writer.writerow([x, y_list[i+1], 4000, 0, 0, 10, -1])
                    sleep(0.01)
                    writer.writerow([x, y_list[i+1], 0, 0, 0, 300, -1])
                    sleep(0.01)

############# for upper
            x_upper_list_p = []
            x_upper_list_n = []
            y_upper_list_p = []
            y_upper_list_n = []
            for i in range(1, self.n_line + 1):
                y_upper_p = self.height//2 + self.n_line // 2 * self.shift
                y_upper_p = y_upper_p - (i - 1) * self.shift
                b = y_upper_p - x
                y_upper_n = y_upper_p - self.width
                y_upper_list_n.append(y_upper_n)
                # print(f"orig y_upper_p: {y_upper_p}\nb: {b}\ny_upper_n: {y_upper_n}")
                if y_upper_p > self.height//2:
                    y_upper_p = self.height//2
                    # print(f"modify y_upper_p: {y_upper_p}")
                    x_upper_p = y_upper_p - b
                    # print(f"b : {b}")
                    x_upper_list_p.append(x_upper_p)
                    y_upper_list_p.append(y_upper_p)
                else:
                    # print(f"modify y_upper_p: {y_upper_p}")
                    x_upper_list_p.append(self.width//2)
                    y_upper_list_p.append(y_upper_p)
            x_upper_list_n = [-x for i in range(self.n_line)]

#             print(f"x_upper_list_p: {x_upper_list_p}\n\
# x_upper_list_n: {x_upper_list_n}\n\
# y_upper_list_p: {y_upper_list_p}\n\
# y_upper_list_n: {y_upper_list_n}")

            y_upper_list = []
            x_upper_list = []
            for i in range(len(y_upper_list_p)):
                y_upper_list.append(y_upper_list_p[i])
                y_upper_list.append(y_upper_list_n[i])
                x_upper_list.append(x_upper_list_p[i])
                x_upper_list.append(x_upper_list_n[i])

            for i in range(0, len(x_upper_list), 2):
                plt.plot(
                    [x_upper_list[i], x_upper_list[i+1]], 
                    [y_upper_list[i], y_upper_list[i+1]], 
                    c='black')
                plt.plot(
                    [-x_upper_list[i], -x_upper_list[i+1]], 
                    [y_upper_list[i], y_upper_list[i+1]], 
                    c='black')

            # save data
            with open(self.orthogonalPath, 'a', newline='') as file:
                writer = csv.writer(file)
                # write center
                for i in range(0, 2*self.n_line, 2):
                    writer.writerow([x_upper_list[i], y_upper_list[i], 0, 0, 0, 300, -1])
                    sleep(0.01)
                    writer.writerow([x_upper_list[i], y_upper_list[i], 4000, 0, 0, 10, -1])
                    sleep(0.01)
                    writer.writerow([x_upper_list[i+1], y_upper_list[i+1], 4000, 0, 0, 10, -1])
                    sleep(0.01)
                    writer.writerow([x_upper_list[i+1], y_upper_list[i+1], 0, 0, 0, 300, -1])
                    sleep(0.01)
                for i in range(0, 2*self.n_line, 2):
                    writer.writerow([-x_upper_list[i], y_upper_list[i], 0, 0, 0, 300, -1])
                    sleep(0.01)
                    writer.writerow([-x_upper_list[i], y_upper_list[i], 4000, 0, 0, 10, -1])
                    sleep(0.01)
                    writer.writerow([-x_upper_list[i+1], y_upper_list[i+1], 4000, 0, 0, 10, -1])
                    sleep(0.01)
                    writer.writerow([-x_upper_list[i+1], y_upper_list[i+1], 0, 0, 0, 300, -1])
                    sleep(0.01)

############# for bottom
            x_bottom_list_p = []
            x_bottom_list_n = []
            y_bottom_list_p = []
            y_bottom_list_n = []
            for i in range(1, self.n_line + 1):
                y_bottom_n = -self.height//2 + self.n_line//2 * self.shift
                y_bottom_n = y_bottom_n - (i - 1) * self.shift
                y_bottom_p = y_bottom_n + self.width
                y_bottom_list_p.append(y_bottom_p)
                b = y_bottom_p - x
                if y_bottom_n < -self.height//2:
                    y_bottom_n = -self.height//2
                    x_bottom_n = (y_bottom_n - b) 
                    x_bottom_list_n.append(x_bottom_n)
                    y_bottom_list_n.append(y_bottom_n)
                else:
                    y_bottom_list_n.append(y_bottom_n)
                    x_bottom_list_n.append(-self.width//2)
            x_bottom_list_p = [x for i in range(self.n_line)]

            y_bottom_list = []
            x_bottom_list = []
            for i in range(len(y_bottom_list_p)):
                y_bottom_list.append(y_bottom_list_p[i])
                y_bottom_list.append(y_bottom_list_n[i])
                x_bottom_list.append(x_bottom_list_p[i])
                x_bottom_list.append(x_bottom_list_n[i])

#             print(f"x_bottom_list_p: {x_bottom_list_p}\n\
# x_bottom_list_n: {x_bottom_list_n}\n\
# y_bottom_list_p: {y_bottom_list_p}\n\
# y_bottom_list_n: {y_bottom_list_n}\n")

            for i in range(0, len(x_bottom_list), 2):
                plt.plot(
                    [x_bottom_list[i], x_bottom_list[i+1]], 
                    [y_bottom_list[i], y_bottom_list[i+1]], 
                    c='black')
                plt.plot(
                    [-x_bottom_list[i], -x_bottom_list[i+1]], 
                    [y_bottom_list[i], y_bottom_list[i+1]], 
                    c='black')

            # save data
            with open(self.orthogonalPath, 'a', newline='') as file:
                writer = csv.writer(file)
                # write center
                for i in range(0, 2*self.n_line, 2):
                    writer.writerow([x_bottom_list[i], y_bottom_list[i], 0, 0, 0, 300, -1])
                    sleep(0.01)
                    writer.writerow([x_bottom_list[i], y_bottom_list[i], 4000, 0, 0, 10, -1])
                    sleep(0.01)
                    writer.writerow([x_bottom_list[i+1], y_bottom_list[i+1], 4000, 0, 0, 10, -1])
                    sleep(0.01)
                    writer.writerow([x_bottom_list[i+1], y_bottom_list[i+1], 0, 0, 0, 300, -1])
                    sleep(0.01)
                for i in range(0, 2*self.n_line, 2):
                    writer.writerow([-x_bottom_list[i], y_bottom_list[i], 0, 0, 0, 300, -1])
                    sleep(0.01)
                    writer.writerow([-x_bottom_list[i], y_bottom_list[i], 4000, 0, 0, 10, -1])
                    sleep(0.01)
                    writer.writerow([-x_bottom_list[i+1], y_bottom_list[i+1], 4000, 0, 0, 10, -1])
                    sleep(0.01)
                    writer.writerow([-x_bottom_list[i+1], y_bottom_list[i+1], 0, 0, 0, 300, -1])
                    sleep(0.01)

            plt.show()


class Ui_Form(Lpg):
    def __init__(self):
        super(Ui_Form, self).__init__()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_height = QtWidgets.QPushButton(Form)
        self.btn_height.setObjectName("btn_height")
        self.verticalLayout_2.addWidget(self.btn_height)
        self.edit_height = QtWidgets.QLineEdit(Form)
        # self.edit_height.setText("")
        self.edit_height.setObjectName("edit_height")
        self.verticalLayout_2.addWidget(self.edit_height)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_width = QtWidgets.QPushButton(Form)
        self.btn_width.setObjectName("btn_width")
        self.verticalLayout_3.addWidget(self.btn_width)
        self.edit_width = QtWidgets.QLineEdit(Form)
        self.edit_width.setObjectName("edit_width")
        self.verticalLayout_3.addWidget(self.edit_width)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btn_indent = QtWidgets.QPushButton(Form)
        self.btn_indent.setObjectName("btn_indent")
        self.verticalLayout_6.addWidget(self.btn_indent)
        self.edit_indent = QtWidgets.QLineEdit(Form)
        self.edit_indent.setObjectName("edit_indent")
        self.verticalLayout_6.addWidget(self.edit_indent)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_shift = QtWidgets.QPushButton(Form)
        self.btn_shift.setObjectName("btn_shift")
        self.verticalLayout_5.addWidget(self.btn_shift)
        self.edit_shift = QtWidgets.QLineEdit(Form)
        self.edit_shift.setObjectName("edit_shift")
        self.verticalLayout_5.addWidget(self.edit_shift)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_n_lines = QtWidgets.QPushButton(Form)
        self.btn_n_lines.setObjectName("btn_n_lines")
        self.verticalLayout_4.addWidget(self.btn_n_lines)
        self.edit_n_lines = QtWidgets.QLineEdit(Form)
        self.edit_n_lines.setObjectName("edit_n_lines")
        self.verticalLayout_4.addWidget(self.edit_n_lines)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btn_orthogonal_pattern = QtWidgets.QPushButton(Form)
        self.btn_orthogonal_pattern.setObjectName("btn_orthogonal_pattern")
        self.verticalLayout.addWidget(self.btn_orthogonal_pattern)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.btn_oblique_pattern = QtWidgets.QPushButton(Form)
        self.btn_oblique_pattern.setObjectName("btn_oblique_pattern")
        self.verticalLayout.addWidget(self.btn_oblique_pattern)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.btn_exit = QtWidgets.QPushButton(Form)
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout.addWidget(self.btn_exit)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.defaultValue()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Linear Pattern Generator"))
        self.btn_height.setText(_translate("Form", "Set Height"))
        self.btn_width.setText(_translate("Form", "Set Width"))
        self.btn_indent.setText(_translate("Form", "Set Indent"))
        self.btn_shift.setText(_translate("Form", "Set Shift"))
        self.btn_n_lines.setText(_translate("Form", "Set # of line"))
        self.btn_orthogonal_pattern.setText(_translate("Form", "Plot Orthogonal Pattern"))
        self.btn_oblique_pattern.setText(_translate("Form", "Plot Oblique Pattern"))
        self.btn_exit.setText(_translate("Form", "Exit"))

        self.btn_shift.clicked.connect(self.getShift)
        self.btn_n_lines.clicked.connect(self.getNlines)
        self.btn_height.clicked.connect(self.getHeight)
        self.btn_width.clicked.connect(self.getWidth)
        self.btn_exit.clicked.connect(self.exitApp)
        self.btn_indent.clicked.connect(self.getIndent)

        self.btn_orthogonal_pattern.clicked.connect(self.orthogonalLine)

        self.edit_height.setReadOnly(True)
        self.edit_width.setReadOnly(True)
        self.edit_shift.setReadOnly(True)
        self.edit_n_lines.setReadOnly(True)
        self.edit_indent.setReadOnly(True)

        QtWidgets.QMessageBox.about(self, "Heads-up!", "\"Unit\" here should be micrometer!")

        # self.link = QtGui.QDesktopServices.openUrl(QtCore.QUrl(
        #     "https://www.youtube.com/embed/xmf-6TYjGuQ"))

    def defaultValue(self):
        self.edit_height.setText("default")
        self.edit_indent.setText("default")
        self.edit_n_lines.setText("default")
        self.edit_shift.setText("default")
        self.edit_width.setText("default")


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()