from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainApp(object):
    def setupUi(self, MainApp):
        MainApp.setObjectName("MainApp")
        MainApp.resize(1017, 805)
        self.centralwidget = QtWidgets.QWidget(MainApp)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_register = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_register.setGeometry(QtCore.QRect(40, 380, 131, 31))
        self.pushButton_register.setObjectName("pushButton_register")
        self.lineEdit_No = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_No.setGeometry(QtCore.QRect(170, 60, 113, 22))
        self.lineEdit_No.setObjectName("lineEdit_No")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(560, 110, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(560, 150, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(560, 180, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(560, 210, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(560, 240, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.comboBox_type = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_type.setGeometry(QtCore.QRect(760, 160, 121, 22))
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_from = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_from.setGeometry(QtCore.QRect(760, 190, 121, 22))
        self.comboBox_from.setObjectName("comboBox_from")
        self.comboBox_from.addItem("")
        self.comboBox_from.addItem("")
        self.comboBox_from.addItem("")
        self.comboBox_from.addItem("")
        self.comboBox_from.addItem("")
        self.comboBox_from.addItem("")
        self.comboBox_dest = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_dest.setGeometry(QtCore.QRect(760, 220, 121, 22))
        self.comboBox_dest.setObjectName("comboBox_dest")
        self.comboBox_dest.addItem("")
        self.comboBox_dest.addItem("")
        self.comboBox_dest.addItem("")
        self.comboBox_dest.addItem("")
        self.comboBox_dest.addItem("")
        self.comboBox_dest.addItem("")
        self.comboBox_entdate = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_entdate.setGeometry(QtCore.QRect(760, 250, 121, 22))
        self.comboBox_entdate.setObjectName("comboBox_entdate")
        self.comboBox_entdate.addItem("")
        self.comboBox_entdate.addItem("")
        self.comboBox_entdate.addItem("")
        self.comboBox_entdate.addItem("")
        self.comboBox_entdate.addItem("")
        self.comboBox_entdate.addItem("")
        self.comboBox_entdate.addItem("")
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(180, 380, 131, 31))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_quit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_quit.setGeometry(QtCore.QRect(320, 380, 131, 31))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 120, 331, 161))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.lineEdit_tcno = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_tcno.setGeometry(QtCore.QRect(180, 120, 113, 22))
        self.lineEdit_tcno.setObjectName("lineEdit_tcno")
        self.lineEdit_name = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_name.setGeometry(QtCore.QRect(180, 60, 113, 22))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_surname = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_surname.setGeometry(QtCore.QRect(180, 90, 113, 22))
        self.lineEdit_surname.setObjectName("lineEdit_surname")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 460, 901, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 10, 101, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        MainApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1017, 26))
        self.menubar.setObjectName("menubar")
        MainApp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainApp)
        self.statusbar.setObjectName("statusbar")
        MainApp.setStatusBar(self.statusbar)

        self.retranslateUi(MainApp)
        QtCore.QMetaObject.connectSlotsByName(MainApp)

    def retranslateUi(self, MainApp):
        _translate = QtCore.QCoreApplication.translate
        MainApp.setWindowTitle(_translate("MainApp", "MainWindow"))
        self.pushButton_register.setText(_translate("MainApp", "Register"))
        self.label.setText(_translate("MainApp", "Track No:"))
        self.label_6.setText(_translate("MainApp", "INFORMATION"))
        self.label_7.setText(_translate("MainApp", "TYPE:"))
        self.label_8.setText(_translate("MainApp", "START POINT:"))
        self.label_9.setText(_translate("MainApp", "DESTINATION:"))
        self.label_10.setText(_translate("MainApp", "ENTRY DATE:"))
        self.comboBox_type.setItemText(0, _translate("MainApp", "-"))
        self.comboBox_type.setItemText(1, _translate("MainApp", "Document"))
        self.comboBox_type.setItemText(2, _translate("MainApp", "Package"))
        self.comboBox_type.setItemText(3, _translate("MainApp", "Letter"))
        self.comboBox_type.setItemText(4, _translate("MainApp", "Other"))
        self.comboBox_from.setItemText(0, _translate("MainApp", "-"))
        self.comboBox_from.setItemText(1, _translate("MainApp", "California"))
        self.comboBox_from.setItemText(2, _translate("MainApp", "New York"))
        self.comboBox_from.setItemText(3, _translate("MainApp", "Texas"))
        self.comboBox_from.setItemText(4, _translate("MainApp", "Ohio"))
        self.comboBox_from.setItemText(5, _translate("MainApp", "Florida"))
        self.comboBox_dest.setItemText(0, _translate("MainApp", "-"))
        self.comboBox_dest.setItemText(1, _translate("MainApp", "California"))
        self.comboBox_dest.setItemText(2, _translate("MainApp", "New York"))
        self.comboBox_dest.setItemText(3, _translate("MainApp", "Texas"))
        self.comboBox_dest.setItemText(4, _translate("MainApp", "Ohio"))
        self.comboBox_dest.setItemText(5, _translate("MainApp", "Florida"))
        self.comboBox_entdate.setItemText(0, _translate("MainApp", "-"))
        self.comboBox_entdate.setItemText(1, _translate("MainApp", "19.11.2020"))
        self.comboBox_entdate.setItemText(2, _translate("MainApp", "20.11.2020"))
        self.comboBox_entdate.setItemText(3, _translate("MainApp", "21.11.2020"))
        self.comboBox_entdate.setItemText(4, _translate("MainApp", "22.11.2020"))
        self.comboBox_entdate.setItemText(5, _translate("MainApp", "23.11.2020"))
        self.comboBox_entdate.setItemText(6, _translate("MainApp", "24.11.2020"))
        self.pushButton_delete.setText(_translate("MainApp", "Delete"))
        self.pushButton_quit.setText(_translate("MainApp", "Exit"))
        self.label_2.setText(_translate("MainApp", "Sender Information"))
        self.label_3.setText(_translate("MainApp", "Name:"))
        self.label_4.setText(_translate("MainApp", "Surname:"))
        self.label_5.setText(_translate("MainApp", "Card No:"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainApp", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainApp", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainApp", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainApp", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainApp", "6"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainApp", "7"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainApp", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainApp", "No"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainApp", "Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainApp", "Surname"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainApp", "Card No"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainApp", "Type"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainApp", "Start Point"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainApp", "Destination"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainApp", "Entry Date"))
        self.pushButton_4.setText(_translate("MainApp", "CREDITS"))

