from PyQt5 import QtGui, QtWidgets 
import sys  
import cocomo 
import math 
import os  


class CocomoApp(QtWidgets.QMainWindow, cocomo.Ui_MainWindow): 
    def __init__(self):
        super(self.__class__, self).__init__()
        self.a = self.b = self.c = self.d = 0
        self.setupUi(self)  
        self.pushButton.clicked.connect(self.calculate)  
                                                            
    def values(self):
        print(f" checked is = {self.model1.currentText()}")
        if self.model1.currentText() == "Organic": 
            self.a = 2.4
            self.b = 1.05
            self.c = 2.5
            self.d = 0.38

        elif self.model1.currentText() == "Semi-Detached": 
            self.a = 3.0
            self.b = 1.12
            self.c = 2.5
            self.d = 0.35

        elif self.model1.currentText() == "Embedded": 
            self.a = 3.6
            self.b = 1.20
            self.c = 2.5
            self.d = 0.32

    def calculate(self):
        self.values()
        loc = float(self.textEdit.toPlainText())
        effort = float(self.a * math.pow(loc, self.b))
        dtime = float(self.c * math.pow(effort, self.d))
        staff = float(effort/dtime)
        productivity = float(loc/effort)
        self.label_6.setText(str(round(effort, 3)))
        self.label_6.setStyleSheet('color: green') 
        self.label_7.setText(str(round(dtime, 3)))
        self.label_7.setStyleSheet('color: green')
        self.label_8.setText(str(round(staff, 3)))
        self.label_8.setStyleSheet('color: green')
        self.label_10.setText(str(round(productivity, 3)))
        self.label_10.setStyleSheet('color: green')


def main():
    app = QtWidgets.QApplication(sys.argv)  
    form = CocomoApp()  
    form.show()  
    sys.exit(app.exec_())  


if __name__ == '__main__':  
    main()  