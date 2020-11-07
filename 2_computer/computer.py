# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'computer.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(581, 539)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd.setStyleSheet("background-color: rgb(170, 170, 0)")
        self.lcd.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcd.setDigitCount(10)
        self.lcd.setObjectName("lcd")
        self.verticalLayout_2.addWidget(self.lcd)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.button_1.setFont(font)
        self.button_1.setObjectName("button_1")
        self.horizontalLayout.addWidget(self.button_1)
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.button_2.setFont(font)
        self.button_2.setObjectName("button_2")
        self.horizontalLayout.addWidget(self.button_2)
        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.button_3.setFont(font)
        self.button_3.setObjectName("button_3")
        self.horizontalLayout.addWidget(self.button_3)
        self.button_plus = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.button_plus.setFont(font)
        self.button_plus.setObjectName("button_plus")
        self.horizontalLayout.addWidget(self.button_plus)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.button_4.setFont(font)
        self.button_4.setObjectName("button_4")
        self.horizontalLayout_2.addWidget(self.button_4)
        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.button_5.setFont(font)
        self.button_5.setObjectName("button_5")
        self.horizontalLayout_2.addWidget(self.button_5)
        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.button_6.setFont(font)
        self.button_6.setObjectName("button_6")
        self.horizontalLayout_2.addWidget(self.button_6)
        self.button_subtract = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.button_subtract.setFont(font)
        self.button_subtract.setObjectName("button_subtract")
        self.horizontalLayout_2.addWidget(self.button_subtract)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.button_7.setFont(font)
        self.button_7.setObjectName("button_7")
        self.horizontalLayout_3.addWidget(self.button_7)
        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.button_8.setFont(font)
        self.button_8.setObjectName("button_8")
        self.horizontalLayout_3.addWidget(self.button_8)
        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.button_9.setFont(font)
        self.button_9.setObjectName("button_9")
        self.horizontalLayout_3.addWidget(self.button_9)
        self.button_multiply = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.button_multiply.setFont(font)
        self.button_multiply.setObjectName("button_multiply")
        self.horizontalLayout_3.addWidget(self.button_multiply)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.button_0.setFont(font)
        self.button_0.setObjectName("button_0")
        self.horizontalLayout_4.addWidget(self.button_0)
        self.button_point = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.button_point.setFont(font)
        self.button_point.setObjectName("button_point")
        self.horizontalLayout_4.addWidget(self.button_point)
        self.button_clear = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.button_clear.setFont(font)
        self.button_clear.setObjectName("button_clear")
        self.horizontalLayout_4.addWidget(self.button_clear)
        self.button_divide = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.button_divide.setFont(font)
        self.button_divide.setObjectName("button_divide")
        self.horizontalLayout_4.addWidget(self.button_divide)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.button_equal = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.button_equal.setFont(font)
        self.button_equal.setObjectName("button_equal")
        self.verticalLayout.addWidget(self.button_equal)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "计算器"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_plus.setText(_translate("MainWindow", "+"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_subtract.setText(_translate("MainWindow", "-"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_multiply.setText(_translate("MainWindow", "*"))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_point.setText(_translate("MainWindow", "."))
        self.button_clear.setText(_translate("MainWindow", "c"))
        self.button_divide.setText(_translate("MainWindow", "/"))
        self.button_equal.setText(_translate("MainWindow", "="))
