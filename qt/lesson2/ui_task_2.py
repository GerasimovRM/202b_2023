# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 462)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 220, 231, 28))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 210, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(270, 40, 127, 116))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.radioButton_2_b = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2_b.setObjectName("radioButton_2_b")
        self.verticalLayout_2.addWidget(self.radioButton_2_b)
        self.radioButton_2_r = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2_r.setObjectName("radioButton_2_r")
        self.verticalLayout_2.addWidget(self.radioButton_2_r)
        self.radioButton_2_g = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2_g.setObjectName("radioButton_2_g")
        self.verticalLayout_2.addWidget(self.radioButton_2_g)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(460, 50, 127, 116))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.radioButton_3_b = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_3_b.setObjectName("radioButton_3_b")
        self.verticalLayout_3.addWidget(self.radioButton_3_b)
        self.radioButton_3_r = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_3_r.setObjectName("radioButton_3_r")
        self.verticalLayout_3.addWidget(self.radioButton_3_r)
        self.radioButton_3_g = QtWidgets.QRadioButton(self.widget1)
        self.radioButton_3_g.setObjectName("radioButton_3_g")
        self.verticalLayout_3.addWidget(self.radioButton_3_g)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(90, 50, 127, 116))
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.radioButton_1_b = QtWidgets.QRadioButton(self.widget2)
        self.radioButton_1_b.setObjectName("radioButton_1_b")
        self.verticalLayout.addWidget(self.radioButton_1_b)
        self.radioButton_1_r = QtWidgets.QRadioButton(self.widget2)
        self.radioButton_1_r.setObjectName("radioButton_1_r")
        self.verticalLayout.addWidget(self.radioButton_1_r)
        self.radioButton_1_g = QtWidgets.QRadioButton(self.widget2)
        self.radioButton_1_g.setObjectName("radioButton_1_g")
        self.verticalLayout.addWidget(self.radioButton_1_g)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label_2.setText(_translate("MainWindow", "Цвет №2"))
        self.radioButton_2_b.setText(_translate("MainWindow", "Синий"))
        self.radioButton_2_r.setText(_translate("MainWindow", "Красный"))
        self.radioButton_2_g.setText(_translate("MainWindow", "Зеленый"))
        self.label_3.setText(_translate("MainWindow", "Цвет №3"))
        self.radioButton_3_b.setText(_translate("MainWindow", "Синий"))
        self.radioButton_3_r.setText(_translate("MainWindow", "Красный"))
        self.radioButton_3_g.setText(_translate("MainWindow", "Зеленый"))
        self.label.setText(_translate("MainWindow", "Цвет №1"))
        self.radioButton_1_b.setText(_translate("MainWindow", "Синий"))
        self.radioButton_1_r.setText(_translate("MainWindow", "Красный"))
        self.radioButton_1_g.setText(_translate("MainWindow", "Зеленый"))
