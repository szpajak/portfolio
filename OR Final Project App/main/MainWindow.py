# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(940, 585)
        MainWindow.setMinimumSize(QtCore.QSize(940, 585))
        MainWindow.setMaximumSize(QtCore.QSize(940, 585))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setWindowTitle('Algorytm Ewolucyjny')
        MainWindow.setWindowIcon(QtGui.QIcon('main/grafiki/PL_LOGO.png'))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(600, 220, 311, 62))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_74 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        self.label_74.setFont(font)
        self.label_74.setObjectName("label_74")
        self.horizontalLayout_2.addWidget(self.label_74)
        self.spinBox_8 = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.spinBox_8.setMinimum(1)
        self.spinBox_8.setMaximum(100)
        self.spinBox_8.setObjectName("spinBox_8")
        self.horizontalLayout_2.addWidget(self.spinBox_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_76 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        self.label_76.setFont(font)
        self.label_76.setObjectName("label_76")
        self.horizontalLayout_3.addWidget(self.label_76)
        self.spinBox_9 = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.spinBox_9.setMaximum(100)
        self.spinBox_9.setObjectName("spinBox_9")
        self.horizontalLayout_3.addWidget(self.spinBox_9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 520, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(229, 239, 0);\n"
"border: none;\n"
"padding-top: 5px;\n"
"color: rgb(60, 4, 57);\n"
"border-right: 3px solid rgb(191, 198, 0);\n"
"border-bottom: 4px solid rgb(191, 198, 0);\n"
"border-left:none;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(238, 243, 0);\n"
"border-right: 3px solid rgb(191, 198, 0);\n"
"border-bottom: 4px solid rgb(191, 198, 0);\n"
"border-left:none;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(206, 213, 0);\n"
"border-left: 4px solid rgb(191, 198, 0);\n"
"border-top: 5px solid rgb(191, 198, 0);\n"
"border-right:none;\n"
"padding-top: -5px;\n"
"border-bottom:none\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(770, 520, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"background-color: rgb(229, 239, 0);\n"
"border: none;\n"
"padding-top: 5px;\n"
"color: rgb(60, 4, 57);\n"
"border-right: 3px solid rgb(191, 198, 0);\n"
"border-bottom: 4px solid rgb(191, 198, 0);\n"
"border-left:none;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(238, 243, 0);\n"
"border-right: 3px solid rgb(191, 198, 0);\n"
"border-bottom: 4px solid rgb(191, 198, 0);\n"
"border-left:none;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(206, 213, 0);\n"
"border-left: 4px solid rgb(191, 198, 0);\n"
"border-top: 5px solid rgb(191, 198, 0);\n"
"border-right:none;\n"
"padding-top: -5px;\n"
"border-bottom:none\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(600, 10, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.layoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(600, 130, 311, 81))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_73 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        self.label_73.setFont(font)
        self.label_73.setObjectName("label_73")
        self.verticalLayout_14.addWidget(self.label_73)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, -1, 123, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.checkBox_11 = QtWidgets.QCheckBox(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        self.checkBox_11.setFont(font)
        self.checkBox_11.setObjectName("checkBox_11")
        self.horizontalLayout_11.addWidget(self.checkBox_11)
        self.verticalLayout_14.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, -1, 132, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_10 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_12.addWidget(self.label_10)
        self.checkBox_12 = QtWidgets.QCheckBox(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        self.checkBox_12.setFont(font)
        self.checkBox_12.setObjectName("checkBox_12")
        self.horizontalLayout_12.addWidget(self.checkBox_12)
        self.verticalLayout_14.addLayout(self.horizontalLayout_12)
        self.layoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(600, 60, 311, 62))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_80 = QtWidgets.QLabel(parent=self.layoutWidget_3)
        self.label_80.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        self.label_80.setFont(font)
        self.label_80.setObjectName("label_80")
        self.horizontalLayout_7.addWidget(self.label_80)
        self.spinBox_12 = QtWidgets.QSpinBox(parent=self.layoutWidget_3)
        self.spinBox_12.setMinimum(1)
        self.spinBox_12.setMaximum(1000)
        self.spinBox_12.setObjectName("spinBox_12")
        self.horizontalLayout_7.addWidget(self.spinBox_12)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_81 = QtWidgets.QLabel(parent=self.layoutWidget_3)
        self.label_81.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        self.label_81.setFont(font)
        self.label_81.setObjectName("label_81")
        self.horizontalLayout_8.addWidget(self.label_81)
        self.spinBox_13 = QtWidgets.QSpinBox(parent=self.layoutWidget_3)
        self.spinBox_13.setMinimum(1)
        self.spinBox_13.setMaximum(1000)
        self.spinBox_13.setObjectName("spinBox_13")
        self.horizontalLayout_8.addWidget(self.spinBox_13)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.layoutWidget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(600, 440, 311, 62))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_78 = QtWidgets.QLabel(parent=self.layoutWidget_4)
        self.label_78.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        self.label_78.setFont(font)
        self.label_78.setObjectName("label_78")
        self.horizontalLayout_4.addWidget(self.label_78)
        self.spinBox_10 = QtWidgets.QSpinBox(parent=self.layoutWidget_4)
        self.spinBox_10.setMaximum(100)
        self.spinBox_10.setSingleStep(0)
        self.spinBox_10.setObjectName("spinBox_10")
        self.horizontalLayout_4.addWidget(self.spinBox_10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_79 = QtWidgets.QLabel(parent=self.layoutWidget_4)
        self.label_79.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        self.label_79.setFont(font)
        self.label_79.setObjectName("label_79")
        self.horizontalLayout_5.addWidget(self.label_79)
        self.spinBox_11 = QtWidgets.QSpinBox(parent=self.layoutWidget_4)
        self.spinBox_11.setMaximum(100)
        self.spinBox_11.setObjectName("spinBox_11")
        self.horizontalLayout_5.addWidget(self.spinBox_11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 271, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("main/grafiki/top_used.png"))
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 100, 561, 451))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("main/grafiki/all_clubs_used.png"))
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(560, 0, 21, 681))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget_5 = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget_5.setGeometry(QtCore.QRect(600, 290, 311, 141))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_77 = QtWidgets.QLabel(parent=self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        font.setBold(True)
        self.label_77.setFont(font)
        self.label_77.setObjectName("label_77")
        self.verticalLayout.addWidget(self.label_77)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, -1, 130, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget_5)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.checkBox_14 = QtWidgets.QCheckBox(parent=self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        self.checkBox_14.setFont(font)
        self.checkBox_14.setObjectName("checkBox_14")
        self.horizontalLayout_6.addWidget(self.checkBox_14)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 164, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget_5)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.checkBox_13 = QtWidgets.QCheckBox(parent=self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        self.checkBox_13.setFont(font)
        self.checkBox_13.setObjectName("checkBox_13")
        self.horizontalLayout.addWidget(self.checkBox_13)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, -1, 53, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(parent=self.layoutWidget_5)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.checkBox_16 = QtWidgets.QCheckBox(parent=self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        self.checkBox_16.setFont(font)
        self.checkBox_16.setObjectName("checkBox_16")
        self.horizontalLayout_10.addWidget(self.checkBox_16)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, -1, 53, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(parent=self.layoutWidget_5)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.checkBox_15 = QtWidgets.QCheckBox(parent=self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        self.checkBox_15.setFont(font)
        self.checkBox_15.setObjectName("checkBox_15")
        self.horizontalLayout_9.addWidget(self.checkBox_15)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 940, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_76.setBuddy(self.spinBox_8)
        self.label_78.setBuddy(self.spinBox_9)
        self.label_79.setBuddy(self.spinBox_10)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.spinBox_11.clear) # type: ignore
        self.pushButton_2.clicked.connect(self.spinBox_10.clear) # type: ignore
        self.pushButton_2.clicked.connect(self.spinBox_9.clear) # type: ignore
        self.pushButton_2.clicked.connect(self.spinBox_8.clear) # type: ignore
        self.pushButton_2.clicked.connect(self.spinBox_13.clear) # type: ignore
        self.pushButton_2.clicked.connect(self.spinBox_12.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.spinBox_12, self.spinBox_13)
        MainWindow.setTabOrder(self.spinBox_13, self.checkBox_11)
        MainWindow.setTabOrder(self.checkBox_11, self.checkBox_12)
        MainWindow.setTabOrder(self.checkBox_12, self.spinBox_8)
        MainWindow.setTabOrder(self.spinBox_8, self.spinBox_9)
        MainWindow.setTabOrder(self.spinBox_9, self.checkBox_14)
        MainWindow.setTabOrder(self.checkBox_14, self.checkBox_13)
        MainWindow.setTabOrder(self.checkBox_13, self.checkBox_16)
        MainWindow.setTabOrder(self.checkBox_16, self.checkBox_15)
        MainWindow.setTabOrder(self.checkBox_15, self.spinBox_10)
        MainWindow.setTabOrder(self.spinBox_10, self.spinBox_11)
        MainWindow.setTabOrder(self.spinBox_11, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Algorytm Ewolucyjny"))
        self.label_74.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Wielkość turnieju/rankingu:</span></p></body></html>"))
        self.label_76.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Procentowa ilość elity:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Oblicz"))
        self.pushButton_2.setText(_translate("MainWindow", "Wyczyść"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Parametry:</span></p></body></html>"))
        self.label_73.setText(_translate("MainWindow", "<html><head/><body><p>Rodzaj selekcji:</p></body></html>"))
        self.checkBox_11.setText(_translate("MainWindow", "Selekcja rankingowa"))
        self.checkBox_12.setText(_translate("MainWindow", "Selekcja turniejowa"))
        self.label_80.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Rozmiar populacji początkowej:</span></p></body></html>"))
        self.label_81.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Liczba pokoleń:</span></p></body></html>"))
        self.label_78.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Procentowa ilość mutacji:</span></p></body></html>"))
        self.label_79.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Stopień mutacji:</span></p></body></html>"))
        self.label_77.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Rodzaje mutacji:</span></p></body></html>"))
        self.checkBox_14.setText(_translate("MainWindow", "Zmiana gospodarza"))
        self.checkBox_13.setText(_translate("MainWindow", "Zmiana kolejki"))
        self.checkBox_16.setText(_translate("MainWindow", "Zmiana godziny 1. część sezonu"))
        self.checkBox_15.setText(_translate("MainWindow", "Zmiana godziny 2. część sezonu"))