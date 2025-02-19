# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\app.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from data import data
from random import choice

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 160)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 201, 131))
        self.groupBox.setObjectName("groupBox")
        self.user_character = QtWidgets.QComboBox(self.groupBox)
        self.user_character.setGeometry(QtCore.QRect(40, 30, 101, 31))
        self.user_character.setObjectName("user_character")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.user_character.addItem("")
        self.run = QtWidgets.QPushButton(self.groupBox)
        self.run.setGeometry(QtCore.QRect(50, 70, 75, 23))
        self.run.setObjectName("run")
        self.output = QtWidgets.QTableWidget(self.centralwidget)
        self.output.setEnabled(True)
        self.output.setGeometry(QtCore.QRect(210, 0, 591, 131))
        self.output.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.output.setObjectName("output")
        self.output.setColumnCount(8)
        self.output.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.output.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.output.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.output.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.output.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.output.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.output.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.output.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.output.setHorizontalHeaderItem(7, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.run.clicked.connect(self.click)# type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def click(self):
        def return_character_data() -> dict:
            char_data = data[self.user_character.currentText()] # get data of character
            # check that data isn't empty
            try:
                if char_data is None:
                    raise ValueError  # raise a value error if data is empty
            except ValueError:
                print("هیچ اطلاعاتی برای این حرف پیدا نشد.")  # show error message to user
                exit()  # exit from app
            return char_data

        character_data = return_character_data()


        def choice_value_of_keys(dictionary: dict) -> dict:
            for key, value in dictionary.items():
                dictionary[key] = choice(value)
            return dictionary

        result = choice_value_of_keys(character_data.copy())

        rowPosition = self.output.rowCount()
        self.output.insertRow(rowPosition)

        self.output.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(self.user_character.currentText()))
        self.output.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(result["name"]))
        self.output.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(result["family"]))
        self.output.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(result["city"]))
        self.output.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(result["country"]))
        self.output.setItem(rowPosition , 5, QtWidgets.QTableWidgetItem(result["color"]))
        self.output.setItem(rowPosition , 6, QtWidgets.QTableWidgetItem(result["food"]))
        self.output.setItem(rowPosition , 7, QtWidgets.QTableWidgetItem(result["things"]))
        # self.output.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "ورودی"))
        self.user_character.setItemText(0, _translate("MainWindow", "ا"))
        self.user_character.setItemText(1, _translate("MainWindow", "ب"))
        self.user_character.setItemText(2, _translate("MainWindow", "پ"))
        self.user_character.setItemText(3, _translate("MainWindow", "ت"))
        self.user_character.setItemText(4, _translate("MainWindow", "ث"))
        self.user_character.setItemText(5, _translate("MainWindow", "ج"))
        self.user_character.setItemText(6, _translate("MainWindow", "چ"))
        self.user_character.setItemText(7, _translate("MainWindow", "ح"))
        self.user_character.setItemText(8, _translate("MainWindow", "خ"))
        self.user_character.setItemText(9, _translate("MainWindow", "د"))
        self.user_character.setItemText(10, _translate("MainWindow", "ذ"))
        self.user_character.setItemText(11, _translate("MainWindow", "ر"))
        self.user_character.setItemText(12, _translate("MainWindow", "ز"))
        self.user_character.setItemText(13, _translate("MainWindow", "ژ"))
        self.user_character.setItemText(14, _translate("MainWindow", "س"))
        self.user_character.setItemText(15, _translate("MainWindow", "ش"))
        self.user_character.setItemText(16, _translate("MainWindow", "ص"))
        self.user_character.setItemText(17, _translate("MainWindow", "ض"))
        self.user_character.setItemText(18, _translate("MainWindow", "ط"))
        self.user_character.setItemText(19, _translate("MainWindow", "ظ"))
        self.user_character.setItemText(20, _translate("MainWindow", "ع"))
        self.user_character.setItemText(21, _translate("MainWindow", "غ"))
        self.user_character.setItemText(22, _translate("MainWindow", "ف"))
        self.user_character.setItemText(23, _translate("MainWindow", "ق"))
        self.user_character.setItemText(24, _translate("MainWindow", "ک"))
        self.user_character.setItemText(25, _translate("MainWindow", "گ"))
        self.user_character.setItemText(26, _translate("MainWindow", "ل"))
        self.user_character.setItemText(27, _translate("MainWindow", "م"))
        self.user_character.setItemText(28, _translate("MainWindow", "ن"))
        self.user_character.setItemText(29, _translate("MainWindow", "و"))
        self.user_character.setItemText(30, _translate("MainWindow", "ه"))
        self.user_character.setItemText(31, _translate("MainWindow", "ی"))
        self.run.setText(_translate("MainWindow", "نشان دادن"))
        item = self.output.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "حرف"))
        item = self.output.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "نام"))
        item = self.output.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "نام خانوادگی"))
        item = self.output.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "شهر"))
        item = self.output.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "کشور"))
        item = self.output.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "رنگ"))
        item = self.output.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "غذا"))
        item = self.output.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "اشیاء"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
