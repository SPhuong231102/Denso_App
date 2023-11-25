from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListView

from Machine_A1 import Ui_history_Window

class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1680, 943)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #CDB7B5")


        self.Select_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Select_Button.setGeometry(QtCore.QRect(30, 330, 451, 141))
        font = QtGui.QFont("Times New Roman")
        font.setPointSize(50)
        self.Select_Button.setFont(font)
        self.Select_Button.setObjectName("Select_Button")
        self.Select_Button.setStyleSheet("QPushButton { background-color: #698B69; color: yellow;  border-radius: 30px }")

        self.Next_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Next_Button.setGeometry(QtCore.QRect(1400, 800, 270, 70))
        self.Next_Button.setObjectName("Next_Button")
        self.Next_Button.setText("Next")
        font = QtGui.QFont("Times New Roman")
        font.setPointSize(50)
        self.Next_Button.setFont(font)
        self.Next_Button.setStyleSheet(" background-color: #698B69; color: yellow;  border-radius: 30px ")

        self.Main_ComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.Main_ComboBox.setGeometry(QtCore.QRect(660, 360, 320, 120))
        self.Main_ComboBox.setObjectName("Main_ComboBox")
        self.Main_ComboBox.setView(QListView())
        self.Main_ComboBox.view().setStyleSheet("QListView::item { height: 150px; width: 100px; }")
        self.Main_ComboBox.setStyleSheet("background-color: #698B69; color: #FEFDA1; font-size: 28px; border-radius: 20px")
        self.Main_ComboBox.addItem("Option")
        self.Main_ComboBox.addItem("Machine A")
        self.Main_ComboBox.addItem("Machine B")
        self.Main_ComboBox.hide()

        self.Second_ComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.Second_ComboBox.setGeometry(QtCore.QRect(70, 300, 181, 41))
        self.Second_ComboBox.setObjectName("Second_ComboBox")
        self.Second_ComboBox.setView(QListView())
        self.Second_ComboBox.view().setStyleSheet("QListView::item { height: 150px; width: 100px; }")
        self.Second_ComboBox.setStyleSheet("background-color: #698B69; color: #FEFDA1; font-size: 28px; border-radius: 20px")
        self.Second_ComboBox.addItem("Option")
        self.Second_ComboBox.addItem("Machine A1")
        self.Second_ComboBox.addItem("Machine A2")
        self.Second_ComboBox.hide()  # Ẩn ComboBox thứ hai ban đầu

        self.Three_ComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.Three_ComboBox.setGeometry(QtCore.QRect(100, 300, 190, 41))
        self.Three_ComboBox.setObjectName("Three_ComboBox")
        self.Three_ComboBox.setView(QListView())
        self.Three_ComboBox.view().setStyleSheet("QListView::item { height: 150px; width: 100px; }")
        self.Three_ComboBox.setStyleSheet("background-color: #698B69; color: #FEFDA1; font-size: 28px; border-radius: 20px")
        self.Three_ComboBox.addItem("Option")
        self.Three_ComboBox.addItem("Machine B1")
        self.Three_ComboBox.addItem("Machine B2")
        self.Three_ComboBox.hide()  # Ẩn ComboBox thứ hai ban đầu

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def showComboBox(self):
        x1, y1 = 660, 360  # Tọa độ mới
        width, height = 320, 60  # Kích thước mới
        self.Main_ComboBox.setGeometry(x1, y1, width, height)
        self.Main_ComboBox.setVisible(not self.Main_ComboBox.isVisible())

    def showSecondComboBox(self,index):
        x2, y2 = 1200, 160  # Tọa độ mới
        width, height = 320, 60  # Kích thước mới
        self.Second_ComboBox.setGeometry(x2, y2, width, height)
        self.Second_ComboBox.setVisible(not self.Second_ComboBox.isVisible())

        selected_option_2 = self.Main_ComboBox.itemText(index)
        if selected_option_2 == "Machine A":
            # self.Second_ComboBox.show()
            self.Three_ComboBox.hide()
            if self.Second_ComboBox.currentText() == "Machine A1":
                self.Next_Button.clicked.connect(self.openWindow_history)
                self.Second_ComboBox.show()
            elif self.Second_ComboBox.currentText() == "Machine A2":
                if __name__ == '__main__':
                    self.openWindow_history()
                    self.Three_ComboBox.show()
            else:
                self.Next_Button.disconnect()
        elif selected_option_2 == "Machine B":
            self.Second_ComboBox.hide()
            self.Three_ComboBox.show()


    def showThreeComboBox(self, index):
        x3, y3 = 1200, 560
        width, height = 320, 61
        self.Three_ComboBox.setGeometry(x3, y3, width, height)
        self.Three_ComboBox.setVisible(not self.Three_ComboBox.isVisible())
        selected_option_3 = self.Main_ComboBox.itemText(index)
        if selected_option_3 == "Machine B":
            self.Three_ComboBox.show()
        else:
            self.Three_ComboBox.hide()

    def openWindow_history(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_history_Window()
        self.ui.setupUi(self.window)
        self.window.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Select_Button.setText(_translate("MainWindow", "Selection Machine"))

        # Kết nối sự kiện click của nút với hàm showComboBox
        self.Select_Button.clicked.connect(self.showComboBox)
        self.Main_ComboBox.currentIndexChanged.connect(self.showSecondComboBox)
        self.Second_ComboBox.currentIndexChanged.connect(self.showSecondComboBox)
        self.Main_ComboBox.currentIndexChanged.connect(self.showThreeComboBox)
        self.Three_ComboBox.currentIndexChanged.connect(self.showThreeComboBox)



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
