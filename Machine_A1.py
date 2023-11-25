

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_history_Window(object):
    def setupUi(self, history_Window):
        history_Window.setObjectName("history_Window")
        history_Window.resize(1680, 943)
        self.centralwidget = QtWidgets.QWidget(history_Window)
        self.centralwidget.setObjectName("centralwidget")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 1661, 891))
        self.groupBox.setObjectName("groupBox")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(0, 90, 631, 801))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(1080, 30, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(48)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(1500, 30, 151, 51))
        self.pushButton.setObjectName("pushButton")

        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(637, 95, 431, 781))
        font = QtGui.QFont()
        font.setFamily("Academy Engraved LET")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.tableWidget_1 = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget_1.setGeometry(QtCore.QRect(1080, 90, 581, 801))
        self.tableWidget_1.setObjectName("tableWidget_1")
        self.tableWidget_1.setColumnCount(4)
        self.tableWidget_1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(3, item)

        history_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(history_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1680, 24))
        self.menubar.setObjectName("menubar")
        history_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(history_Window)
        self.statusbar.setObjectName("statusbar")
        history_Window.setStatusBar(self.statusbar)

        self.retranslateUi(history_Window)
        QtCore.QMetaObject.connectSlotsByName(history_Window)

    def retranslateUi(self, history_Window):
        _translate = QtCore.QCoreApplication.translate
        history_Window.setWindowTitle(_translate("history_Window", "MainWindow"))
        self.groupBox.setTitle(_translate("history_Window", "GroupBox"))
        self.label.setText(_translate("history_Window", " Display Information"))
        self.label_2.setText(_translate("history_Window", "Image"))
        self.label_3.setText(_translate("history_Window", "History"))
        self.pushButton.setText(_translate("history_Window", "Configure"))
        self.label_4.setText(_translate("history_Window", " Result Key Information Extract"))
        item = self.tableWidget_1.horizontalHeaderItem(0)
        item.setText(_translate("history_Window", "Name File"))
        item = self.tableWidget_1.horizontalHeaderItem(1)
        item.setText(_translate("history_Window", "Data Modified"))
        item = self.tableWidget_1.horizontalHeaderItem(2)
        item.setText(_translate("history_Window", "Address"))
        item = self.tableWidget_1.horizontalHeaderItem(3)
        item.setText(_translate("history_Window", "Processing"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    history_Window = QtWidgets.QMainWindow()
    ui = Ui_history_Window()
    ui.setupUi(history_Window)
    history_Window.show()
    sys.exit(app.exec_())
