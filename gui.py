# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Stepan\Desktop\игститут\СПБПУ\Графика\pix\test.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1706, 1156)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #22222e\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(40, 959, 111, 41))
        self.checkBox.setStyleSheet(" display: inline-block;\n"
"  border-radius: 4px;\n"
"  background-color: #f4511e;\n"
"  border: none;\n"
"  color: #FFFFFF;\n"
"  text-align: center;\n"
"  font-size: 14px;\n"
"  padding: 10px;\n"
"  width: 200px;\n"
"  transition: all 0.5s;\n"
"  cursor: pointer;\n"
"  margin: 5px;")
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 1010, 191, 81))
        self.pushButton.setStyleSheet("QPushButton {\n"
"  display: inline-block;\n"
"  border-radius: 4px;\n"
"  background-color: #f4511e;\n"
"  border: none;\n"
"  color: #FFFFFF;\n"
"  text-align: center;\n"
"  font-size: 28px;\n"
"  padding: 20px;\n"
"  width: 200px;\n"
"  transition: all 0.5s;\n"
"  cursor: pointer;\n"
"  margin: 5px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(180, 100, 1281, 781))
        self.label.setMouseTracking(True)
        self.label.setTabletTracking(False)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\Stepan\\Desktop\\игститут\\СПБПУ\\Графика\\pix\\def.jpg"))
        self.label.setObjectName("label")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(150, 960, 111, 41))
        self.checkBox_2.setStyleSheet(" display: inline-block;\n"
"  border-radius: 4px;\n"
"  background-color: #f4511e;\n"
"  border: none;\n"
"  color: #FFFFFF;\n"
"  text-align: center;\n"
"  font-size: 14px;\n"
"  padding: 10px;\n"
"  width: 200px;\n"
"  transition: all 0.5s;\n"
"  cursor: pointer;\n"
"  margin: 5px;")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(260, 960, 121, 41))
        self.checkBox_3.setStyleSheet(" display: inline-block;\n"
"  border-radius: 4px;\n"
"  background-color: #f4511e;\n"
"  border: none;\n"
"  color: #FFFFFF;\n"
"  text-align: center;\n"
"  font-size: 14px;\n"
"  padding: 10px;\n"
"  width: 200px;\n"
"  transition: all 0.5s;\n"
"  cursor: pointer;\n"
"  margin: 5px;")
        self.checkBox_3.setObjectName("checkBox_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(1150, 950, 381, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"  border-radius: 4px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1540, 950, 121, 31))
        self.pushButton_2.setStyleSheet("  display: inline-block;\n"
"  padding: 0px 0px;\n"
"  font-size:20px;\n"
"  cursor: pointer;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  outline: none;\n"
"  color: #fff;\n"
"  background-color: #4CAF50;\n"
"  border: none;\n"
"  border-radius: 4px;\n"
"  box-shadow: 0 9px #999;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(490, 10, 601, 61))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"  border-radius: 4px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1540, 890, 121, 41))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"  display: inline-block;\n"
"  border-radius: 4px;\n"
"  background-color: #f4511e;\n"
"  border: none;\n"
"  color: #FFFFFF;\n"
"  text-align: center;\n"
"  font-size: 20px;\n"
"  padding: 0px;\n"
"  width: 200px;\n"
"  transition: all 0.5s;\n"
"  cursor: pointer;\n"
"  margin: 5px;\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1540, 1020, 121, 31))
        self.pushButton_3.setStyleSheet("  display: inline-block;\n"
"  padding: 0px 0px;\n"
"  font-size:20px;\n"
"  cursor: pointer;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  outline: none;\n"
"  color: #fff;\n"
"  background-color: #4CAF50;\n"
"  border: none;\n"
"  border-radius: 4px;\n"
"  box-shadow: 0 9px #999;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(1150, 1020, 381, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"  border-radius: 4px;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 1010, 201, 81))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"  display: inline-block;\n"
"  border-radius: 4px;\n"
"  background-color: #f4511e;\n"
"  border: none;\n"
"  color: #FFFFFF;\n"
"  text-align: center;\n"
"  font-size: 28px;\n"
"  padding: 20px;\n"
"  width: 200px;\n"
"  transition: all 0.5s;\n"
"  cursor: pointer;\n"
"  margin: 5px;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1706, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MyProg"))
        self.checkBox.setText(_translate("MainWindow", "Человек"))
        self.pushButton.setText(_translate("MainWindow", "Поиск"))
        self.checkBox_2.setText(_translate("MainWindow", "Собака"))
        self.checkBox_3.setText(_translate("MainWindow", "Машина"))
        self.pushButton_2.setText(_translate("MainWindow", "Файл"))
        self.pushButton_4.setText(_translate("MainWindow", "Скачать"))
        self.pushButton_3.setText(_translate("MainWindow", "Фон"))
        self.pushButton_5.setText(_translate("MainWindow", "Совместить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
