# -*- coding: utf-8 -*-

import sys

from pandas import read_excel
from matplotlib.pyplot import subplots, tight_layout, show

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QFileDialog, QApplication
from PyQt5.QtCore import QMetaObject, QCoreApplication

class Ui_Form(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.path = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 150)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.loadDataPushButton = QPushButton(Form)
        self.loadDataPushButton.setObjectName("loadDataPushButton")
        self.verticalLayout.addWidget(self.loadDataPushButton)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.convertPushButton = QPushButton(Form)
        self.convertPushButton.setObjectName("convertPushButton")
        self.verticalLayout.addWidget(self.convertPushButton)
        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.loadDataPushButton.setText(_translate("Form", "Load Data"))
        self.convertPushButton.setText(_translate("Form", "Convert"))

        self.loadDataPushButton.clicked.connect(self.openFileNameDialog)
        self.convertPushButton.clicked.connect(self.draw)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.path, _ = QFileDialog.getOpenFileName( self,
                                                    "Choose a file",
                                                    "",
                                                    "All Files (*);;Excel (*.xls, *.xlsm, *.xlsx)",
                                                    options = options)

    def draw(self):
        df = read_excel(self.path, header=None, encoding='utf-8')
        ax = []
        for i in range(len(df.columns)):
            ax.append(f'ax{i}')

        _, ax = subplots(len(df.columns), sharex=True, sharey=True, gridspec_kw={'hspace': 0}, figsize=(15, 6))

        for i in range(len(df.columns)):
            x = range(len(df.iloc[2:, i]))
            ax[i].plot(x, df.iloc[2:, i], label=f'{df.iloc[0, i]}->{df.iloc[1, i]}')
            ax[i].legend(loc=0)
            ax[i].set_xticks(x)

        ax[0].set_title("Visualised WF")
        tight_layout()
        show()


def main():
    app = QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()