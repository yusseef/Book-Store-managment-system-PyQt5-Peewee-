from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import sys
import sqlite3

MainUi, _ = loadUiType('main.ui')


class Main(QMainWindow, MainUi):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db_connection()
        self.cur = self.db.cursor()
        self.handle_buttons()
        self.ui_changes()
        self.all_books()
        self.all_clients()
        self.all_employee()
        self.daily_movement()
        self.show_emp()
        self.show_loan_bonus()
        self.show_today()
        self.show_client()
        #self.remove_client()






    def ui_changes(self):
        # Ui in log in page
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.tabBar().setVisible(False)
        self.comboBox.model().item(0).setEnabled(False)
        self.lineEdit_43.setText("0")
        self.lineEdit_44.setText("0")
        self.comboBox_3.model().item(0).setEnabled(False)
        self.comboBox_4.model().item(0).setEnabled(False)
        self.comboBox_6.model().item(0).setEnabled(False)
        self.comboBox_2.model().item(0).setEnabled(False)





    def db_connection(self):
        # database connection
        try:
            self.db = sqlite3.connect('library.db')
        except:
            QMessageBox.about(self, "Warning", "database error")
    def handle_buttons(self):
        # handle buttons in app

        self.pushButton.clicked.connect(self.open_daily_movement)
        self.pushButton_2.clicked.connect(self.open_books)
        self.pushButton_5.clicked.connect(self.open_clients)
        self.pushButton_4.clicked.connect(self.open_settings)
        self.pushButton_6.clicked.connect(self.open_cs)
        self.pushButton_24.clicked.connect(self.open_home)
        self.pushButton_25.clicked.connect(self.open_home)

        self.pushButton_27.clicked.connect(self.open_home)
        self.pushButton_28.clicked.connect(self.open_home)
        self.pushButton_13.clicked.connect(self.open_home)
        self.pushButton_78.clicked.connect(self.open_clients)
        self.pushButton_81.clicked.connect(self.open_clients)

        self.pushButton_96.clicked.connect(self.open_clients)
        self.pushButton_101.clicked.connect(self.open_clients)
        self.pushButton_79.clicked.connect(self.open_settings)
        self.pushButton_82.clicked.connect(self.open_settings)
        self.pushButton_87.clicked.connect(self.open_settings)
        self.pushButton_102.clicked.connect(self.open_settings)
        self.pushButton_80.clicked.connect(self.open_books)
        self.pushButton_86.clicked.connect(self.open_books)
        self.pushButton_97.clicked.connect(self.open_books)
        self.pushButton_104.clicked.connect(self.open_books)
        self.pushButton_76.clicked.connect(self.open_cs)
        self.pushButton_84.clicked.connect(self.open_cs)
        self.pushButton_89.clicked.connect(self.open_cs)
        self.pushButton_99.clicked.connect(self.open_cs)
        self.pushButton_85.clicked.connect(self.open_daily_movement)
        self.pushButton_90.clicked.connect(self.open_daily_movement)
        self.pushButton_100.clicked.connect(self.open_daily_movement)
        self.pushButton_105.clicked.connect(self.open_daily_movement)
        self.pushButton_7.clicked.connect(self.daily_movement)
        self.pushButton_23.clicked.connect(self.handle_login)
        self.pushButton_30.clicked.connect(self.open_login)
        #database buttons

        self.pushButton_14.clicked.connect(self.remove_client)
        self.pushButton_14.clicked.connect(self.all_clients)
        self.pushButton_22.clicked.connect(self.remove_emp)
        self.pushButton_22.clicked.connect(self.all_employee)
        self.pushButton_18.clicked.connect(self.remove_book)
        self.pushButton_18.clicked.connect(self.all_books)




        self.pushButton_12.clicked.connect(self.add_clients)
        self.pushButton_12.clicked.connect(self.show_client)
        self.pushButton_16.clicked.connect(self.add_employee)
        self.pushButton_12.clicked.connect(self.all_clients)
        self.pushButton_16.clicked.connect(self.all_employee)
        self.pushButton_7.clicked.connect(self.today)
        self.pushButton_7.clicked.connect(self.show_today)
        self.pushButton_8.clicked.connect(self.add_book)
        self.pushButton_8.clicked.connect(self.all_books)
        self.pushButton_8.clicked.connect(self.daily_movement)
        self.pushButton_16.clicked.connect(self.show_emp)
        self.pushButton_71.clicked.connect(self.loan_bonus)
        self.pushButton_71.clicked.connect(self.show_loan_bonus)








    def handle_login(self):
        # handle log in page
        user = self.lineEdit_9.text()
        password = self.lineEdit_16.text()
        query = "SELECT * From Users where Name=? and Password=?"
        data = self.cur.execute(query, (user, password))
        if len(self.cur.fetchall()) > 0:
            self.tabWidget.setCurrentIndex(1)
        else:
            QMessageBox.about(self, "Warning", "Wrong user name or password")
        #today permission#####
        today_query = "SELECT today_permission from Users where Name=? and Password=? "
        today_data=self.cur.execute(today_query, (user, password))
        if self.cur.fetchone() == ('0',):
            self.pushButton.setEnabled(False)
            self.pushButton_85.setEnabled(False)
            self.pushButton_90.setEnabled(False)
            self.pushButton_100.setEnabled(False)
            self.pushButton_105.setEnabled(False)
        #books_permission
        books_query = "SELECT books_permission from Users where Name=? and Password=?"
        books_data = self.cur.execute(books_query, (user, password))
        if self.cur.fetchone() == ('0',):
            self.pushButton_2.setEnabled(False)
            self.pushButton_80.setEnabled(False)
            self.pushButton_86.setEnabled(False)
            self.pushButton_97.setEnabled(False)
            self.pushButton_104.setEnabled(False)
        #client_permission
        client_query = "SELECT client_permission from Users where Name=? and Password=?"
        client_data = self.cur.execute(client_query, (user, password))
        if self.cur.fetchone() == ('0',):
            self.pushButton_5.setEnabled(False)
            self.pushButton_78.setEnabled(False)
            self.pushButton_81.setEnabled(False)
            self.pushButton_96.setEnabled(False)
            self.pushButton_101.setEnabled(False)
        #setting_permissions
        setting_query = "SELECT setting_permission from Users where Name=? and Password=?"
        setting_data = self.cur.execute(setting_query, (user, password))
        if self.cur.fetchone() == ('0',):
            self.pushButton_4.setEnabled(False)
            self.pushButton_79.setEnabled(False)
            self.pushButton_82.setEnabled(False)
            self.pushButton_87.setEnabled(False)
            self.pushButton_102.setEnabled(False)


    def daily_movement(self):
        # handle today tab
        try:
            query = "SELECT Book_name FROM Books"
            data = self.cur.execute(query)
            for i in data:
                self.comboBox.addItem(str(i)[2:(len(str(i)))-3])
            query1 = "SELECT Book_name FROM Books"
            data1 = self.cur.execute(query)
            for i in data1:
                self.comboBox_3.addItem(str(i)[2:(len(str(i))) - 3])
        except:
            QMessageBox.about(self, "Warning", "Program crashed")
    def today(self):
        try:
            qty = self.spinBox.value()
            name = (self.comboBox.currentText())
            user = self.lineEdit_9.text()
            query = self.cur.execute("SELECT Price FROM Books WHERE Book_name='"+name+"';")
            x = str((query.fetchone()))[1:len(str(query.fetchone()))-1]
            y = int(x)
            price = qty*y
            self.lineEdit_18.setText(str(price))
            self.cur.execute("INSERT INTO today(book_title , qty , price , name) VALUES(? , ? , ? , ?)",(name, qty, price,user))
            self.db.commit()
        except:
            QMessageBox.about(self, "Warning", "you must choose book name")
    def show_today(self):
        try:
            query = "SELECT * FROM today"
            result = self.cur.execute(query)
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colum_number, QTableWidgetItem(str(data)))
        except:
            QMessageBox.about(self, "Warning", "program crashed")
    def loan_bonus(self):
        try:
            name = self.comboBox_2.currentText()
            loan = self.lineEdit_43.text()
            bonus = self.lineEdit_44.text()
            query = self.cur.execute("SELECT Salary FROM Users WHERE Name='"+name+"';")
            x = str((query.fetchone()))[1:len(str(query.fetchone())) + 1]
            y = int(x)
            print(y)
            final = (y +int(bonus))- int(loan)
            print(final)
            self.cur.execute("INSERT INTO loan_bonus(User_name , loan , bonus , final_salary) VALUES(? , ? , ? , ?)",(name, loan, bonus, final))
            self.db.commit()
        except:
            QMessageBox.about(self, "Warning", "Choose employee name")

    def show_loan_bonus(self):
        try:
            query = "SELECT * FROM loan_bonus"
            result = self.cur.execute(query)
            self.tableWidget_10.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget_10.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.tableWidget_10.setItem(row_number, colum_number, QTableWidgetItem(str(data)))
        except:
            QMessageBox.about(self, "Warning", "program crashed")
    # BOOK TAB ######################

    def all_books(self):
        # all books tab
        try:
            query = "SELECT * FROM Books"
            result = self.cur.execute(query)
            self.tableWidget_2.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget_2.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.tableWidget_2.setItem(row_number, colum_number, QTableWidgetItem(str(data)))
        except:
            QMessageBox.about(self, "Warning", "program crashed")
    def add_book(self):
        # Add books
        try:
            book_name = self.lineEdit_3.text()
            book_description = self.lineEdit_4.text()
            price = self.lineEdit_15.text()
            qty = self.lineEdit_12.text()
            added = self.lineEdit_9.text()

            self.cur.execute("INSERT INTO Books(Book_name , Price , Book_description , qty , added) VALUES(? , ? , ? , ? , ?)"
                            ,(book_name, price, book_description, qty, added))
            self.db.commit()
        except:
            QMessageBox.about(self, "Warning", "There are field has string input and you insert int input or opposite")
    # #############
    # Clients TAB ######################

    def all_clients(self):
        # all clients tab
        try:
            query1 = "SELECT * FROM Client"
            result1 = self.cur.execute(query1)
            self.tableWidget_3.setRowCount(0)
            for row_number1, row_data1 in enumerate(result1):
                self.tableWidget_3.insertRow(row_number1)
                for colum_number1, data1 in enumerate(row_data1):
                    self.tableWidget_3.setItem(row_number1, colum_number1, QTableWidgetItem(str(data1)))
        except:
            QMessageBox.about(self, "Warning", "program crashed")
    def add_clients(self):
        # Add clients
        try:
            client_name = self.lineEdit_8.text()
            client_phone = self.lineEdit_11.text()
            client_mail = self.lineEdit_10.text()
            client_age = self.lineEdit_17.text()
            added = self.lineEdit_9.text()
            self.cur.execute("INSERT INTO Client(Name , PhoneNumber , Age , email , added) VALUES(? , ? , ? , ? , ?)",
                             (client_name, client_phone, client_age, client_mail, added))
            self.db.commit()
        except:
            QMessageBox.about(self, "Warning", "Must fill all fields,Or filed must have int input and you add string input")
    #############################
    # settings TAB ######################

    def add_employee(self):
        # Add employee
        try:
            emp_name = self.lineEdit_31.text()
            emp_phone = self.lineEdit_32.text()
            emp_mail = self.lineEdit_33.text()
            emp_password = self.lineEdit_34.text()
            emp_salary = self.lineEdit_45.text()
            emp_job_title = self.lineEdit_46.text()

            if self.checkBox_16.isChecked() is True:
                books_permission = 1
            else:
                books_permission = 0

            if self.checkBox_15.isChecked() is True:
                Clients_permission = 1
            else:
                Clients_permission = 0

            if self.checkBox_17.isChecked() is True:
                Settings_permission = 1
            else:
                Settings_permission = 0

            if self.checkBox_13.isChecked() is True:
                today_permission = 1
            else:
                today_permission = 0

            self.cur.execute("INSERT INTO Users(Name , PhoneNumber , email , Password , Salary ,"
                             " Job_title , today_permission , "
                             "books_permission , client_permission, setting_permission) "
                             "Values(? , ? , ? , ? , ? , ? , ? , ? , ? , ?)",(emp_name, emp_phone, emp_mail, emp_password, emp_salary, emp_job_title, today_permission, books_permission, Clients_permission, Settings_permission))
            self.db.commit()
        except:
            QMessageBox.about(self, "Warning", "important fields are missing")
    def all_employee(self):
        try:
            query4 = "SELECT * FROM Users"
            result4 = self.cur.execute(query4)
            self.tableWidget_9.setRowCount(0)
            for row_number4, row_data4 in enumerate(result4):
                self.tableWidget_9.insertRow(row_number4)
                for colum_number4, data4 in enumerate(row_data4):
                    self.tableWidget_9.setItem(row_number4, colum_number4, QTableWidgetItem(str(data4)))
        except:
            QMessageBox.about(self, "Warning", "program crashed")
    def show_emp(self):
        try:
            query = "SELECT Name FROM Users"
            data = self.cur.execute(query)
            for i in data:
                self.comboBox_2.addItem(str(i)[2:(len(str(i))) - 3])
            query1 = "SELECT Name FROM Users"
            data1 = self.cur.execute(query1)
            for i in data:
                self.comboBox_6.addItem(str(i)[2:(len(str(i))) - 3])
        except:
            QMessageBox.about(self, "Warning", "program crashed")
    def show_client(self):
        try:
            query = "SELECT Name FROM Client"
            data = self.cur.execute(query)
            for i in data:
                self.comboBox_4.addItem(str(i)[2:(len(str(i))) - 3])
        except:
            QMessageBox.about(self, "Warning", "program crashed")
    def remove_client(self):
        try:
            data = self.comboBox_4.currentText()
            self.cur.execute("DELETE FROM Client WHERE Name='" + data+ "';")
            self.db.commit()
        except:
            QMessageBox.about(self, "Warning", "program crashed")
    def remove_emp(self):
        try:
            data = self.comboBox_6.currentText()
            self.cur.execute("DELETE FROM Users WHERE Name='" + data+ "';")
            self.db.commit()
        except:
            QMessageBox.about(self, "Warning", "program crashed")
    def remove_book(self):
        try:
            data = self.comboBox_3.currentText()
            self.cur.execute("DELETE FROM Books WHERE Book_name='" + data + "';")
            self.db.commit()
        except:
            QMessageBox.about(self, "Warning", "program crashed")

    def open_login(self):
        self.tabWidget.setCurrentIndex(0)

    def open_daily_movement(self):
        self.tabWidget.setCurrentIndex(2)

    def open_books(self):
        self.tabWidget.setCurrentIndex(3)
        self.tabWidget_2.setCurrentIndex(0)

    def open_clients(self):
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_3.setCurrentIndex(0)

    def open_settings(self):
        self.tabWidget.setCurrentIndex(5)
        self.tabWidget_4.setCurrentIndex(0)

    def open_cs(self):
        self.tabWidget.setCurrentIndex(6)

    ##############
    def open_home(self):
        self.tabWidget.setCurrentIndex(1)


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

