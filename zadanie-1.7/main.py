# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerweUasA.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import matplotlib.pyplot
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import pyqtgraph as pg
import sys
import matplotlib.pyplot as plt
import numpy as np
import math

class showSin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sin')
        layout = QVBoxLayout()
        self.label = QLabel()

        x = np.arange(0, 4 * np.pi - 1, 0.1)  # start,stop,step
        y = np.sin(x)
        plt.plot(x, y)
        plt.xlabel('x values from 0 to 4pi')  # string must be enclosed with quotes '  '
        plt.ylabel('sin(x)')
        plt.title('Plot of sin from 0 to 4pi')
        plt.legend(['sin(x)'])  # legend entries as seperate strings in a list
        plt.savefig('img/sin.png')
        plt.show()

        pixmap = QPixmap("img/sin.png")
        self.label.setPixmap(pixmap)
        layout.addWidget(self.label)
        self.setLayout(layout)

class showCos(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cos')
        layout = QVBoxLayout()
        self.label = QLabel()

        x = np.arange(0, 4 * np.pi - 1, 0.1)  # start,stop,step
        y = np.cos(x)
        plt.plot(x, y)
        plt.xlabel('x values from 0 to 4pi')  # string must be enclosed with quotes '  '
        plt.ylabel('sin(x)')
        plt.title('Plot of cos from 0 to 4pi')
        plt.legend(['cos(x)'])  # legend entries as seperate strings in a list
        plt.savefig('img/cos.png')
        plt.show()

        pixmap = QPixmap("img/sin.png")
        self.label.setPixmap(pixmap)
        layout.addWidget(self.label)
        self.setLayout(layout)

class showTg(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tg')
        layout = QVBoxLayout()
        x = np.linspace(-2 * math.pi, 2 * math.pi, 1000)
        y = np.tan(x)
        y[:-1][np.diff(y) < 0] = np.nan
        plt.grid()
        plt.xlabel("x")
        plt.ylabel("$tg(x)$")
        plt.ylim(-10, 10)
        plt.xlim(-2 * math.pi, 2 * math.pi)
        radian_multiples = [-2, -3 / 2, -1, -1 / 2, 0, 1 / 2, 1, 3 / 2, 2]
        radians = [n * math.pi for n in radian_multiples]
        radian_labels = ['$-2\pi$', '$-3\pi/2$', '$\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$']
        plt.xticks(radians, radian_labels)
        plt.title("$y = tg(x)$", fontsize=14)
        plt.plot(x, y)
        plt.savefig('img/tg.png')
        plt.show()

        self.label = QLabel()
        pixmap = QPixmap("img/tg.png")
        self.label.setPixmap(pixmap)
        layout.addWidget(self.label)
        self.setLayout(layout)

class showCtg(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ctg')
        layout = QVBoxLayout()
        x = np.linspace(-2 * math.pi, 2 * math.pi, 1000)
        y = np.tan(x)
        y[:-1][np.diff(y) < 0] = np.nan
        plt.grid()
        plt.xlabel("x")
        plt.ylabel("$ctg(x)$")
        plt.ylim(-10, 10)
        plt.xlim(-2 * math.pi, 2 * math.pi)
        radian_multiples = [-2, -3 / 2, -1, -1 / 2, 0, 1 / 2, 1, 3 / 2, 2]
        radians = [n * math.pi for n in radian_multiples]
        radian_labels = ['$-2\pi$', '$-3\pi/2$', '$\pi$', '$-\pi/2$', '0', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$']
        plt.xticks(radians, radian_labels)
        plt.title("$y = ctg(x)$", fontsize=14)
        plt.plot(x, 1/y)
        plt.savefig('img/ctg.png')
        plt.show()

        self.label = QLabel()
        pixmap = QPixmap("img/ctg.png")
        self.label.setPixmap(pixmap)
        layout.addWidget(self.label)
        self.setLayout(layout)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(810, 880)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.bSin = QPushButton(self.centralwidget)
        self.bSin.setObjectName(u"bSin")

        self.gridLayout.addWidget(self.bSin, 0, 0, 1, 1)

        self.b9 = QPushButton(self.centralwidget)
        self.b9.setObjectName(u"b9")

        self.gridLayout.addWidget(self.b9, 0, 3, 1, 1)

        self.bDziel = QPushButton(self.centralwidget)
        self.bDziel.setObjectName(u"bDziel")

        self.gridLayout.addWidget(self.bDziel, 0, 4, 1, 1)

        self.b7 = QPushButton(self.centralwidget)
        self.b7.setObjectName(u"b7")

        self.gridLayout.addWidget(self.b7, 0, 1, 1, 1)

        self.b8 = QPushButton(self.centralwidget)
        self.b8.setObjectName(u"b8")

        self.gridLayout.addWidget(self.b8, 0, 2, 1, 1)

        self.bCos = QPushButton(self.centralwidget)
        self.bCos.setObjectName(u"bCos")

        self.gridLayout.addWidget(self.bCos, 1, 0, 1, 1)

        self.bTg = QPushButton(self.centralwidget)
        self.bTg.setObjectName(u"bTg")

        self.gridLayout.addWidget(self.bTg, 2, 0, 1, 1)

        self.b4 = QPushButton(self.centralwidget)
        self.b4.setObjectName(u"b4")

        self.gridLayout.addWidget(self.b4, 1, 1, 1, 1)

        self.b1 = QPushButton(self.centralwidget)
        self.b1.setObjectName(u"b1")

        self.gridLayout.addWidget(self.b1, 2, 1, 1, 1)

        self.b5 = QPushButton(self.centralwidget)
        self.b5.setObjectName(u"b5")

        self.gridLayout.addWidget(self.b5, 1, 2, 1, 1)

        self.b2 = QPushButton(self.centralwidget)
        self.b2.setObjectName(u"b2")

        self.gridLayout.addWidget(self.b2, 2, 2, 1, 1)

        self.b6 = QPushButton(self.centralwidget)
        self.b6.setObjectName(u"b6")

        self.gridLayout.addWidget(self.b6, 1, 3, 1, 1)

        self.bMnoz = QPushButton(self.centralwidget)
        self.bMnoz.setObjectName(u"bMnoz")

        self.gridLayout.addWidget(self.bMnoz, 1, 4, 1, 1)

        self.bMinus = QPushButton(self.centralwidget)
        self.bMinus.setObjectName(u"bMinus")

        self.gridLayout.addWidget(self.bMinus, 2, 4, 1, 1)

        self.b3 = QPushButton(self.centralwidget)
        self.b3.setObjectName(u"b3")

        self.gridLayout.addWidget(self.b3, 2, 3, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.b0 = QPushButton(self.centralwidget)
        self.b0.setObjectName(u"b0")

        self.gridLayout_2.addWidget(self.b0, 0, 1, 1, 1)

        self.bCtg = QPushButton(self.centralwidget)
        self.bCtg.setObjectName(u"bCtg")

        self.gridLayout_2.addWidget(self.bCtg, 0, 0, 1, 1)

        self.bDot = QPushButton(self.centralwidget)
        self.bDot.setObjectName(u"bDot")

        self.gridLayout_2.addWidget(self.bDot, 0, 2, 1, 1)

        self.bPlus = QPushButton(self.centralwidget)
        self.bPlus.setObjectName(u"bPlus")

        self.gridLayout_2.addWidget(self.bPlus, 0, 3, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bC = QPushButton(self.centralwidget)
        self.bC.setObjectName(u"bC")

        self.horizontalLayout.addWidget(self.bC)

        self.bRowna = QPushButton(self.centralwidget)
        self.bRowna.setObjectName(u"bRowna")

        self.horizontalLayout.addWidget(self.bRowna)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 810, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # C L I C K E D
        self.b7.clicked.connect(lambda: self.wpisz7())
        self.b8.clicked.connect(lambda: self.wpisz8())
        self.b9.clicked.connect(lambda: self.wpisz9())
        self.bDziel.clicked.connect(lambda: self.dzielenie())

        self.b4.clicked.connect(lambda: self.wpisz4())
        self.b5.clicked.connect(lambda: self.wpisz5())
        self.b6.clicked.connect(lambda: self.wpisz6())
        self.bMnoz.clicked.connect(lambda: self.mnozenie())

        self.b1.clicked.connect(lambda: self.wpisz1())
        self.b2.clicked.connect(lambda: self.wpisz2())
        self.b3.clicked.connect(lambda: self.wpisz3())
        self.bMinus.clicked.connect(lambda: self.odejmowanie())

        self.b0.clicked.connect(lambda: self.wpisz0())
        self.bDot.clicked.connect(lambda: self.wpisz13())
        self.bPlus.clicked.connect(lambda: self.dodawanie())

        self.bC.clicked.connect(lambda: self.clearSth())
        self.bRowna.clicked.connect(lambda: self.wynik())

        self.bSin.clicked.connect(lambda: self.showSin())
        self.bCos.clicked.connect(lambda: self.showCos())
        self.bTg.clicked.connect(lambda: self.showTg())
        self.bCtg.clicked.connect(lambda: self.showCtg())




        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bSin.setText(QCoreApplication.translate("MainWindow", u"sin", None))
        self.b9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.bDziel.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.b7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.b8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.bCos.setText(QCoreApplication.translate("MainWindow", u"cos", None))
        self.bTg.setText(QCoreApplication.translate("MainWindow", u"tg", None))
        self.b4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.b1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.b5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.b2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.b6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.bMnoz.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.bMinus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.b3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.b0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bCtg.setText(QCoreApplication.translate("MainWindow", u"ctg", None))
        self.bDot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.bPlus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.bC.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.bRowna.setText(QCoreApplication.translate("MainWindow", u"=", None))

    # D E F S
    def showSin(self):
        if (self.lineEdit.text() == ''):
            self.lineEdit.setText("")
        else:
            try:
                haha = math.sin(int(self.lineEdit.text()))
                self.lineEdit.setText(str(haha))
            except:
                self.lineEdit.setText("")
                print("prosze nie uzywac niepotrzebnych znakow")
        self.window = showSin()
        self.window.show()

    def showCos(self):
        if (self.lineEdit.text() == ''):
            self.lineEdit.setText("")
        else:
            try:
                haha = math.cos(int(self.lineEdit.text()))
                self.lineEdit.setText(str(haha))
            except:
                self.lineEdit.setText("")
                print("prosze nie uzywac niepotrzebnych znakow")
        self.window = showCos()
        self.window.show()
    def showTg(self):
        if (self.lineEdit.text() == ''):
            self.lineEdit.setText("")
        else:
            try:
                haha = math.tan(int(self.lineEdit.text()))
                self.lineEdit.setText(str(haha))
            except:
                self.lineEdit.setText("")
                print("prosze nie uzywac niepotrzebnych znakow")
        self.window = showTg()
        self.window.show()
    def showCtg(self):
        if (self.lineEdit.text() == ''):
            self.lineEdit.setText("")
        else:
            try:
                haha = math.tan(int(self.lineEdit.text()))
                self.lineEdit.setText(str(1/haha))
            except:
                self.lineEdit.setText("")
                print("prosze nie uzywac niepotrzebnych znakow")
        self.window = showCtg()
        self.window.show()

    def clearSth(self):
        self.lineEdit.clear()
        self.enabled()

    def wpisz0(self):
        self.lineEdit.insert("0")
        self.enabled()

    def wpisz1(self):
        self.lineEdit.insert("1")
        self.enabled()

    def wpisz2(self):
        self.lineEdit.insert("2")
        self.enabled()

    def wpisz3(self):
        self.lineEdit.insert("3")
        self.enabled()

    def wpisz4(self):
        self.lineEdit.insert("4")
        self.enabled()

    def wpisz5(self):
        self.lineEdit.insert("5")
        self.enabled()

    def wpisz6(self):
        self.lineEdit.insert("6")
        self.enabled()

    def wpisz7(self):
        self.lineEdit.insert("7")
        self.enabled()

    def wpisz8(self):
        self.lineEdit.insert("8")
        self.enabled()

    def wpisz9(self):
        self.lineEdit.insert("9")
        self.enabled()

    def wpisz13(self):
        if (self.lineEdit.text() == ''):
            self.lineEdit.setText("")
        else:
            self.lineEdit.insert(".")
            self.disabled()

    def dodawanie(self):
        if (self.lineEdit.text() == ''):
            self.lineEdit.setText("")
        else:
            self.lineEdit.insert("+")
            self.disabledMinus()

    def odejmowanie(self):
        if (self.lineEdit.text() == '-'):
            self.lineEdit.setText("")
        else:
            self.lineEdit.insert("-")
            self.disabledMinus()

    def mnozenie(self):
        if (self.lineEdit.text() == ''):
            self.lineEdit.setText("")
        else:
            self.lineEdit.insert("*")
            self.disabledMinus()

    def dzielenie(self):
        if (self.lineEdit.text() == ''):
            self.lineEdit.setText("")
        else:
            self.lineEdit.insert("/")
            self.disabledMinus()

    def wynik(self):
        if (self.lineEdit.text() == ''):
            self.lineEdit.setText("")
        else:
            try:
                haha = eval(self.lineEdit.text())
                self.lineEdit.setText(str(haha))
            except ZeroDivisionError:
                self.lineEdit.setText("")
                print("nie mozna dzielic przez 0")
            else:
                self.lineEdit.setText(str(haha))

    def disabled(self):
        self.bDziel.setDisabled(True)
        self.bMnoz.setDisabled(True)
        self.bMinus.setDisabled(True)
        self.bDot.setDisabled(True)
        self.bPlus.setDisabled(True)

    def disabledMinus(self):
        self.bDziel.setDisabled(True)
        self.bMnoz.setDisabled(True)
        self.bDot.setDisabled(True)
        self.bPlus.setDisabled(True)

    def enabled(self):
        self.bDziel.setDisabled(False)
        self.bMnoz.setDisabled(False)
        self.bMinus.setDisabled(False)
        self.bDot.setDisabled(False)
        self.bPlus.setDisabled(False)
    # retranslateUi

