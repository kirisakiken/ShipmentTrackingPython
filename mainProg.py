import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTableWidgetItem

from MainApp import *


global curs
global con

app = QtWidgets.QApplication(sys.argv)

MainWindow_App = QtWidgets.QMainWindow()
Ui_MainApp = Ui_MainApp()
Ui_MainApp.setupUi(MainWindow_App)
MainWindow_App.show()

con = sqlite3.connect('maindb.db')
curs = con.cursor()

curs.execute("CREATE TABLE IF NOT EXISTS tblDATA (ID INTEGER not null primary key autoincrement, KargoNo TEXT not null, Adı TEXT not null, Soyadı TEXT not null, TC TEXT not null, Cinsi TEXT not null, Hareket TEXT not null, Varış TEXT not null, Tarih TEXT not null)")
con.commit()



def addData():
    
    newData_no = Ui_MainApp.lineEdit_No.text()
    newData_name = Ui_MainApp.lineEdit_name.text()
    newData_surname = Ui_MainApp.lineEdit_surname.text()
    newData_tc = Ui_MainApp.lineEdit_tcno.text()
    newData_type = Ui_MainApp.comboBox_type.currentText()
    newData_from = Ui_MainApp.comboBox_from.currentText()
    newData_dest = Ui_MainApp.comboBox_dest.currentText()
    newData_date = Ui_MainApp.comboBox_entdate.currentText()
    
    curs.execute("INSERT INTO tblDATA(KargoNo, Adı, Soyadı, TC, Cinsi, Hareket, Varış, Tarih) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (newData_no, newData_name, newData_surname, newData_tc, newData_type, newData_from, newData_dest, newData_date))
    con.commit()
    
    reWrite()

def deleteData():
    
    LF = Ui_MainApp.lineEdit_No.text()
    
    curs.execute("DELETE FROM tblDATA WHERE KargoNo = {}".format(LF))
    con.commit()
    
    reWrite()

def reWrite():
    
    data = curs.execute("SELECT * FROM tblDATA")
    
    Ui_MainApp.tableWidget.clear()
    
    fdata = data.fetchall()
    expander = len(fdata)
    
    for row, columnvalues in enumerate(fdata):
        
        for column, value in enumerate(columnvalues):
            
            Ui_MainApp.tableWidget.setItem(row, column, QTableWidgetItem(str(value)))
            
            if (int(expander) > 6):
        
                Ui_MainApp.tableWidget.setRowCount(expander)

def voidExit():
    
    sys.exit(app.exec_())


reWrite()

















Ui_MainApp.pushButton_register.clicked.connect(addData)
Ui_MainApp.pushButton_delete.clicked.connect(deleteData)
Ui_MainApp.pushButton_quit.clicked.connect(voidExit)


sys.exit(app.exec_())






