# import sys
# from PyQt5 import QtCore, QtGui, QtWidgets

# class inputdialogdemo(QtWidgets.QWidget):
#    def __init__(self, parent = None):
#       super(inputdialogdemo, self).__init__(parent)
		
#       layout = QtWidgets.QFormLayout()
#       self.btn = QtWidgets.QPushButton("Choose from list")
#       self.btn.clicked.connect(self.getItem)
		
#       self.le = QtWidgets.QLineEdit()
#       layout.addRow(self.btn,self.le)
#       self.btn1 = QtWidgets.QPushButton("get name")
#       self.btn1.clicked.connect(self.gettext)
		
#       self.le1 = QtWidgets.QLineEdit()
#       layout.addRow(self.btn1,self.le1)
#       self.btn2 = QtWidgets.QPushButton("Enter an integer")
#       self.btn2.clicked.connect(self.getint)
		
#       self.le2 = QtWidgets.QLineEdit()
#       layout.addRow(self.btn2,self.le2)
#       self.setLayout(layout)
#       self.setWindowTitle("Input Dialog demo")
		
#    def getItem(self):
#       items = ("C", "C++", "Java", "Python")
		
#       item, ok = QtWidgets.QInputDialog.getItem(self, "select input dialog", 
#          "list of languages", items, 0, False)
			
#       if ok and item:
#          self.le.setText(item)
			
#    def gettext(self):
#       text, ok = QtWidgets.QInputDialog.getText(self, 'Text Input Dialog', 'Enter your name:')
		
#       if ok:
#          self.le1.setText(str(text))
			
#    def getint(self):
#       num,ok = QtWidgets.QInputDialog.getInt(self,"integer input dualog","enter a number")
		
#       if ok:
#          self.le2.setText(str(num))
#          print(f'answer\'s here: {num}')
			
# def main(): 
#    app = QtWidgets.QApplication(sys.argv)
#    ex = inputdialogdemo()
#    ex.show()
#    sys.exit(app.exec_())
	
# if __name__ == '__main__':
#    main()

#############################################################

# !/usr/bin/env python
# -*- coding: utf-8 -*-

# import sys
# from PyQt5 import QtWidgets, QtCore, QtGui


# class MyPopup(QtWidgets.QWidget):
#    def __init__(self):
#       QtWidgets.QWidget.__init__(self)

#    def paintEvent(self, e):
#       dc = QtWidgets.QPainter(self)
#       dc.drawLine(0, 0, 100, 100)
#       dc.drawLine(100, 0, 0, 100)

# class MainWindow(QtWidgets.QMainWindow):
#    def __init__(self, *args):
#       QtWidgets.QMainWindow.__init__(self, *args)
#       self.cw = QtWidgets.QWidget(self)
#       self.setCentralWidget(self.cw)
#       self.btn1 = QtWidgets.QPushButton("Click me", self.cw)
#       self.btn1.setGeometry(QtCore.QRect(0, 0, 100, 30))
#       self.connect(self.btn1, QtWidgets.SIGNAL("clicked()"), self.doit)
#       self.w = None

#    def doit(self):
#       print ("Opening a new popup window...")
#       self.w = MyPopup()
#       self.w.setGeometry(QtWidgets.QRect(100, 100, 400, 200))
#       self.w.show()

# class App(QtWidgets.QApplication):
#    def __init__(self, *args):
#       QtWidgets.QApplication.__init__(self, *args)
#       self.main = MainWindow()
#       self.connect(self, QtWidgets.SIGNAL("lastWindowClosed()"), self.byebye )
#       self.main.show()

#    def byebye( self ):
#       self.exit(0)

# def main(args):
#    global app
#    app = App(args)
#    app.exec_()

# if __name__ == "__main__":
#    main(sys.argv)


######################################################################

# import matplotlib.pyplot as plt
# import math
# import numpy as np

# a = 100
# b = 80
# x_list = []
# y_list = []
# l = np.linspace(-math.pi, math.pi, 500)

# for i in l:
#    x = a * math.cos(i)
#    y = b * math.sin(i)
#    x_list.append(x)
#    y_list.append(y)

# plt.plot(x_list, y_list)
# plt.show()

############################################

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QFontComboBox, QLineEdit, QMessageBox, QVBoxLayout


# class Demo(QWidget):
#    choice = 'a'
#    choice_list = ['b', 'c', 'd', 'e']

#    def __init__(self):
#       super(Demo, self).__init__()

#       self.combobox_1 = QComboBox(self)                   # 1
#       self.combobox_2 = QFontComboBox(self)               # 2

#       self.lineedit = QLineEdit(self)                     # 3

#       self.v_layout = QVBoxLayout()

#       self.layout_init()
#       self.combobox_init()

#    def layout_init(self):
#       self.v_layout.addWidget(self.combobox_1)
#       self.v_layout.addWidget(self.combobox_2)
#       self.v_layout.addWidget(self.lineedit)

#       self.setLayout(self.v_layout)

#    def combobox_init(self):
#       self.combobox_1.addItem(self.choice)              # 4
#       self.combobox_1.addItems(self.choice_list)        # 5
#       self.combobox_1.currentIndexChanged.connect(lambda: self.on_combobox_func(self.combobox_1))   # 6
#       # self.combobox_1.currentTextChanged.connect(lambda: self.on_combobox_func(self.combobox_1))  # 7

#       self.combobox_2.currentFontChanged.connect(lambda: self.on_combobox_func(self.combobox_2))

#    def on_combobox_func(self, combobox):                                                             # 8
#       if combobox == self.combobox_1:
#             QMessageBox.information(self, 'ComboBox 1', '{}: {}'.format(combobox.currentIndex(), combobox.currentText()))
#       else:
#             self.lineedit.setFont(combobox.currentFont())


# if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    demo = Demo()
#    demo.show()
#    sys.exit(app.exec_())



################################################

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QSpinBox, QDoubleSpinBox, QHBoxLayout


# class Demo(QWidget):
#    def __init__(self):
#       super(Demo, self).__init__()
#       self.spinbox = QSpinBox(self)
#       self.spinbox.setRange(-99, 99)                                                      # 1
#       self.spinbox.setSingleStep(1)                                                       # 2
#       self.spinbox.setValue(66)                                                           # 3
#       self.spinbox.valueChanged.connect(self.value_change_func)                           # 4

#       self.double_spinbox = QDoubleSpinBox(self)                                          # 5
#       self.double_spinbox.setRange(-99.99, 99.99)
#       self.double_spinbox.setSingleStep(0.01)
#       self.double_spinbox.setValue(66.66)

#       self.h_layout = QHBoxLayout()
#       self.h_layout.addWidget(self.spinbox)
#       self.h_layout.addWidget(self.double_spinbox)
#       self.setLayout(self.h_layout)

#    def value_change_func(self):
#       decimal_part = self.double_spinbox.value() - int(self.double_spinbox.value())       # 6
#       self.double_spinbox.setValue(self.spinbox.value() + decimal_part)                   # 7


# if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    demo = Demo()
#    demo.show()
#    sys.exit(app.exec_())


###################################

# from PyQt5.QtWidgets import QWidget,QHBoxLayout,QTableWidget,QPushButton,QApplication,QVBoxLayout,QTableWidgetItem,QCheckBox,QAbstractItemView,QHeaderView,QLabel,QFrame
# from PyQt5 import QtWidgets
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QFont,QColor
# import random
# import sys
# class ui(QWidget):
#    def __init__(self):
#       super().__init__()
#       self.setupUI()
#       self.id = 1
#       self.lines = []
#       self.editable = True
#       self.des_sort = True
#       #self.faker = Factory.create()
#       self.btn_add.clicked.connect(self.add_line)
#       self.btn_del.clicked.connect(self.del_line)
#       self.btn_rep.clicked.connect(self.rep_line)
#       self.combox1 = QtWidgets.QComboBox(self)
#       self.combox1.addItem('a')
#       self.combox1.addItems(['b', 'c'])

#    def setupUI(self):
#       self.setWindowTitle('WF Calculator')
#       self.resize(640,480)
#       self.table = QTableWidget(self)
#       self.btn_add = QPushButton('Add')
#       self.btn_del = QPushButton('Delete')
#       self.btn_rep = QPushButton('Repeat')
#       self.vbox = QVBoxLayout()
#       self.vbox.addWidget(self.btn_add)
#       self.vbox.addWidget(self.btn_del)
#       self.vbox.addWidget(self.btn_rep)
#       self.txt = QLabel()
#       self.txt.setMinimumHeight(50)
#       self.vbox2 = QVBoxLayout()
#       self.vbox2.addWidget(self.table)
#       self.vbox2.addWidget(self.txt)
#       self.hbox = QHBoxLayout()
#       self.hbox.addLayout(self.vbox2)
#       self.hbox.addLayout(self.vbox)
#       self.setLayout(self.hbox)
#       self.table.setColumnCount(4)   ##設置列數
#       self.headers = ['id','select','voltage','frames']
#       self.table.setHorizontalHeaderLabels(self.headers)

#    def add_line(self):
#       row = self.table.rowCount()
#       self.table.setRowCount(row + 1)
#       id = str(self.id)
#       ck = QCheckBox()
#       h = QHBoxLayout()
#       h.setAlignment(Qt.AlignCenter)
#       h.addWidget(ck)
#       w = QWidget()
#       w.setLayout(h)
#       #name = self.faker.name()
#       #score = str(random.randint(50,99))
#       #add = self.faker.address()
#       self.table.setItem(row,0,QTableWidgetItem(id))
#       self.table.setCellWidget(row,1,w)
#       #self.table.setItem(row,2,QTableWidgetItem(name))
#       #self.table.setItem(row,3,QTableWidgetItem(score))
#       #self.table.setItem(row,4,QTableWidgetItem(add))
#       self.id += 1
#       self.lines.append([id, ck, self.combox1, "b"])

#    def del_line(self):
#       removeline = []
#       for line in self.lines:
#             if line[1].isChecked():
#                row = self.table.rowCount()
#                for x in range(row,0,-1):
#                   if line[0] == self.table.item(x - 1,0).text():
#                         self.table.removeRow(x - 1)
#                         removeline.append(line)
#       for line in removeline:
#             self.lines.remove(line)


#    def rep_line(self):
#       repeatline = []
#       for line in self.lines:
#             if line[1].isChecked():
#                row = self.table.rowCount()
#                for x in range(row,0,-1):
#                   if line[0] == self.table.item(x - 1,0).text():
#                         self.table.removeRow(x - 1)
#                         repeatline.append(line)
#       for line in repeatline:
#             self.lines.repeat(line)


# if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    ui = ui()
#    ui.show()
#    sys.exit(app.exec_())


######################################################################
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

   def __init__(self):
      super().__init__()
      self.title = 'PyQt5 textbox - pythonspot.com'
      self.left = 10
      self.top = 10
      self.width = 400
      self.height = 140
      self.initUI()
   
   def initUI(self):
      self.setWindowTitle(self.title)
      self.setGeometry(self.left, self.top, self.width, self.height)
   
      # Create textbox
      self.textbox = QLineEdit(self)
      self.textbox.move(20, 20)
      self.textbox.resize(280,40)
      
      # Create a button in the window
      self.button = QPushButton('Show text', self)
      self.button.move(20,80)
      
      # connect button to function on_click
      self.button.clicked.connect(self.on_click)
      self.show()
   
   @pyqtSlot()
   def on_click(self):
      textboxValue = self.textbox.text()
      QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
      self.textbox.setText("")

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = App()
   sys.exit(app.exec_())