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

import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class MyPopup(QtWidgets.QWidget):
   def __init__(self):
      QtWidgets.QWidget.__init__(self)

   def paintEvent(self, e):
      dc = QtWidgets.QPainter(self)
      dc.drawLine(0, 0, 100, 100)
      dc.drawLine(100, 0, 0, 100)

class MainWindow(QtWidgets.QMainWindow):
   def __init__(self, *args):
      QtWidgets.QMainWindow.__init__(self, *args)
      self.cw = QtWidgets.QWidget(self)
      self.setCentralWidget(self.cw)
      self.btn1 = QtWidgets.QPushButton("Click me", self.cw)
      self.btn1.setGeometry(QtCore.QRect(0, 0, 100, 30))
      self.connect(self.btn1, QtWidgets.SIGNAL("clicked()"), self.doit)
      self.w = None

   def doit(self):
      print ("Opening a new popup window...")
      self.w = MyPopup()
      self.w.setGeometry(QtWidgets.QRect(100, 100, 400, 200))
      self.w.show()

class App(QtWidgets.QApplication):
   def __init__(self, *args):
      QtWidgets.QApplication.__init__(self, *args)
      self.main = MainWindow()
      self.connect(self, QtWidgets.SIGNAL("lastWindowClosed()"), self.byebye )
      self.main.show()

   def byebye( self ):
      self.exit(0)

def main(args):
   global app
   app = App(args)
   app.exec_()

if __name__ == "__main__":
   main(sys.argv)


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

