# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sk2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 250)
        MainWindow.setMaximumSize(QtCore.QSize(250, 250))
        MainWindow.setStyleSheet("QMainWindow{background-image: url(bn_240.png)}\n"
"/*QMainWindow{background-image: url(/path/of/image)}*/")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt2 = QtWidgets.QPushButton(self.centralwidget)
        self.bt2.setGeometry(QtCore.QRect(140, 60, 61, 61))
        self.bt2.setMinimumSize(QtCore.QSize(61, 61))
        self.bt2.setMaximumSize(QtCore.QSize(61, 61))
        self.bt2.setText("")
        self.bt2.setIconSize(QtCore.QSize(60, 60))
        self.bt2.setObjectName("bt2")
        self.btx = QtWidgets.QPushButton(self.centralwidget)
        self.btx.setGeometry(QtCore.QRect(30, 150, 21, 21))
        self.btx.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.btx.setText("")
        self.btx.setObjectName("btx")
        self.bt1 = QtWidgets.QPushButton(self.centralwidget)
        self.bt1.setGeometry(QtCore.QRect(50, 60, 61, 61))
        self.bt1.setMinimumSize(QtCore.QSize(61, 61))
        self.bt1.setMaximumSize(QtCore.QSize(61, 61))
        self.bt1.setText("")
        self.bt1.setIconSize(QtCore.QSize(60, 60))
        self.bt1.setObjectName("bt1")
        self.bt3 = QtWidgets.QPushButton(self.centralwidget)
        self.bt3.setGeometry(QtCore.QRect(100, 140, 61, 61))
        self.bt3.setMinimumSize(QtCore.QSize(61, 61))
        self.bt3.setMaximumSize(QtCore.QSize(61, 61))
        self.bt3.setText("")
        self.bt3.setIconSize(QtCore.QSize(60, 60))
        self.bt3.setObjectName("bt3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
# import a_rc
