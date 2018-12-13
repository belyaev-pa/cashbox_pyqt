# -*- coding: utf-8 -*-
import sys
import datetime
from decimal import getcontext, Decimal
#from PyQt4.QtGui import *
#from PyQt4.QtCore import *
#from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import  QMainWindow, QMenu, QAction, QMessageBox, QDialog
from PyQt5.QtGui import  QStandardItem
from PyQt5.QtCore import  QVariant
from PyQt5 import  QtCore
from PyQt5.QtWidgets import QLabel, QTextEdit, QApplication
from PyQt5.QtCore import QSettings
#from PyQt5.QtWidgets import QMenu, QAction

#from PyQt5.QtWidgets import (QWidget,QHBoxLayout,QVBoxLayout, QToolTip,
#    QPushButton,QDesktopWidget, QApplication, QTextEdit)
#from PyQt5.QtGui import QFont
from main import MainWidget
from dialog import *
from dbmodel import *
from setting_dialog import SettingsDialog

class Window(QMainWindow):
    defaults = {'addressDBServerEdit': 'localhost',
                'portDBServerEdit': '5432',
                'usingDBEdit': 'postgresql+psycopg2',
                'userNameEdit': 'postgres',
                'userPasswordEdit': '1111',
                'baseNameEdit': 'testbase',
                'cashboxNameEdit': 'cashbox1'
                }
    check_price = Decimal('0.00')
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.engine = create_engine(db_connect(), echo=True)
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

        self.settings = QSettings('project')

        self.main_show()
        self.add_menu()
        self.auth_action()

        getcontext().prec = 4

    def main_show(self):
        self.win = MainWidget()
        self.setCentralWidget(self.win)
        self.win.barcodeEdit.setFocus()
        self.win.barcodeEdit.returnPressed.connect(self.add_position)

        self.win.delete_btn.clicked.connect(self.delete_action)
        self.win.cancel_btn.clicked.connect(self.cancel_action)
        self.win.in_btn.clicked.connect(self.in_action)
        self.win.out_btn.clicked.connect(self.out_action)
        self.win.report_btn.clicked.connect(self.report_action)
        self.win.close_btn.clicked.connect(self.close_action)
        self.win.increment_btn.clicked.connect(self.increment_action)
        self.win.total_btn.clicked.connect(self.total_action)

        self.statusBar().showMessage("Касса")

    def add_menu(self):
        self.menuSettings = QMenu("Настройки")
        self.actSettings_change = QAction("Основные", None)
        self.actSettings_change.triggered.connect(self.on_clicked_settings_change)
        self.menuSettings.addAction(self.actSettings_change)
        self.menuBar().addMenu(self.menuSettings)

    def add_position(self):
        try:
            barcode = str(self.win.barcodeEdit.text())
        except:
            QMessageBox.critical(window, "Ошибка",
                                 "Некорректный штрихкод",
                                 buttons=QMessageBox.Ok,
                                 defaultButton=QMessageBox.Ok)
            self.win.barcodeEdit.setText('')
        else:
            find_list = self.win.table_model.findItems(str(barcode), column=0)
            if not find_list:
            	try:
                	product = self.session.query(Product).filter(
                    	Product.barcode == barcode).first()
                except:
                    QMessageBox.critical(window, "Ошибка",
                                 "Такого товара в базе нет",
                                 buttons=QMessageBox.Ok,
                                 defaultButton=QMessageBox.Ok)
                    self.win.barcodeEdit.setText('')
                else:
                	list_x = [QStandardItem(str(product.barcode)),
                    	      QStandardItem(str(product.name)),
                        	  QStandardItem(str(1)),
                          	  QStandardItem(str(product.purchase_price)),
                         	  ]
                	self.win.table_model.appendRow(list_x)
                	self.win.barcodeEdit.setText('')
                	self.win.barcodeEdit.setFocus()
                	self.win.table.resizeColumnsToContents()
                	self.check_price = Decimal(
                    	str(product.purchase_price)) + Decimal(self.check_price)
                	self.win.totalEdit.setText(str(self.check_price))
            else:
                for obj in find_list:
                    count = self.win.table_model.item(obj.row(), 2).text()
                    price = self.win.table_model.item(obj.row(), 3).text()
                    count = int(count)+1
                    self.win.table_model.setItem(int(obj.row()), 
                                                 2, 
                                                 QStandardItem(str(count)))
                    self.win.barcodeEdit.setText('')
                    self.win.barcodeEdit.setFocus()
                    self.win.table.resizeColumnsToContents()
                    self.check_price += Decimal(str(price))
                    self.win.totalEdit.setText(str(self.check_price))

    def delete_action(self):
        self.dialog = DeleteDialog(window)
        self.index = self.win.table.currentIndex()
        self.dialog.deleteEdit.setText(str('string: ')+str(self.index.row()))
        self.result = self.dialog.exec_()
        if self.result == QDialog.Accepted:
            if self.index.isValid():
                count = self.win.table_model.item(self.index.row(), 2).text()
                price = self.win.table_model.item(self.index.row(), 3).text()
                self.check_price = Decimal(self.check_price) - (
                    Decimal(str(price))*Decimal(str(count)))
                self.win.totalEdit.setText(str(self.check_price))
                self.win.table_model.removeRow(self.index.row())
                self.win.barcodeEdit.setText('')
                self.win.barcodeEdit.setFocus()
            else:
                QMessageBox.critical(self, "Ошибка",
                                     "Некорректная строка",
                                     buttons=QMessageBox.Ok,
                                     defaultButton=QMessageBox.Ok)
                self.delete_action()

    def cancel_action(self):
        self.dialog = CancelDialog(window)
        self.result = self.dialog.exec_()
        if self.result == QDialog.Accepted:
            self.win.table_model.clear()
            self.win.table_model.setHorizontalHeaderLabels(
                self.win.table_head_attr_list)
            self.win.barcodeEdit.setText('')
            self.win.barcodeEdit.setFocus()
            self.check_price = Decimal('0.00')
            self.win.totalEdit.setText(str(Decimal(self.check_price)))

    def increment_action(self):
        self.dialog = MultiIncrementDialog(window)
        self.index = self.win.table.currentIndex()
        self.result = self.dialog.exec_()
        if self.result == QDialog.Accepted:
            if self.index.isValid():
                try:
                    count = int(self.dialog.incrementEdit.text())
                except:
                    QMessageBox.critical(self, "Ошибка",
                                         "Некорректное количество",
                                         buttons=QMessageBox.Ok,
                                         defaultButton=QMessageBox.Ok)
                    self.increment_action()
                else:
                    count_now = self.win.table_model.item(
                        self.index.row(), 2).text()
                    price = self.win.table_model.item(
                        self.index.row(), 3).text()
                    decrement = Decimal(str(price)) * Decimal(str(count_now))
                    increment = Decimal(str(price)) * Decimal(str(count))
                    self.check_price = Decimal(self.check_price) - Decimal(
                        decrement) + Decimal(increment)
                    self.win.totalEdit.setText(str(self.check_price))
                    self.win.table_model.setItem(int(self.index.row()), 
                                                 2,
                                                 QStandardItem(str(count)))
                    self.win.barcodeEdit.setText('')
                    self.win.barcodeEdit.setFocus()
            else:
                QMessageBox.critical(self, "Ошибка",
                                     "Некорректная строка",
                                     buttons=QMessageBox.Ok,
                                     defaultButton=QMessageBox.Ok)
                self.increment_action()

    def first_in_action(self):
        self.dialog = FirstInDialog()
        self.result = self.dialog.exec_()
        if self.result == QDialog.Accepted:
            try:
                self.first_in = Decimal(float(self.dialog.inputEdit.text()))
            except:
                QMessageBox.critical(self, "Ошибка",
                                     "Некорректная сумма //",
                                     buttons=QMessageBox.Ok,
                                     defaultButton=QMessageBox.Ok)
                self.first_in_action()
            else:
                cashbox_value = self.settings.value('cashboxNameEdit',
                                 QVariant(self.defaults['cashboxNameEdit']))
                #cashbox_value = cashbox_value.toPyObject()
                #print(cashbox_value)
                cashbox = self.session.query(CashBox).filter(
                    CashBox.id == 1).first()
                c_id = int(cashbox.id)
                self.report = Report(c_id, self.user_id)
                self.session.add(self.report)
                self.session.commit()
                self.check_price = Decimal('0.00')
                self.win.totalEdit.setText(str(Decimal(self.check_price)))
        else:
            QMessageBox.critical(self, "Ошибка",
                                 "Нельзя начать работу без внесения",
                                 buttons=QMessageBox.Ok,
                                 defaultButton=QMessageBox.Ok)
            self.first_in_action()

    def in_action(self):
        self.dialog = InDialog(window)
        self.result = self.dialog.exec_()
        if self.result == QDialog.Accepted:
            try:
                in_sum = Decimal(self.dialog.inputEdit.text())
            except:
                QMessageBox.critical(window, "Ошибка",
                                     "Некорректная сумма",
                                     buttons=QMessageBox.Ok,
                                     defaultButton=QMessageBox.Ok)
                self.in_action()
            else:
                self.report.amendment = Decimal(self.report.amendment)+in_sum
                self.session.commit()
                self.win.barcodeEdit.setFocus()

    def out_action(self):
        self.dialog = OutDialog(window)
        self.result = self.dialog.exec_()
        if self.result == QDialog.Accepted:
            try:
                out_sum = Decimal(self.dialog.outputEdit.text())
            except:
                QMessageBox.critical(window, "Ошибка",
                                     "Некорректная сумма",
                                     buttons=QMessageBox.Ok,
                                     defaultButton=QMessageBox.Ok)
                self.out_action()
            else:
                self.report.withdrawal = Decimal(self.report.withdrawal)+out_sum
                self.session.commit()
                self.win.barcodeEdit.setFocus()

    def report_action(self):
        self.dialog = ReportDialog(window)
        self.result = self.dialog.exec_()
        if self.result == QDialog.Accepted:
            pass # report print function

    def close_action(self):
        self.dialog = CloseDialog(window)
        self.result = self.dialog.exec_()
        if self.result == QDialog.Accepted:
            pass

    def total_action(self):
        self.dialog = CloseDialog(window)
        self.result = self.dialog.exec_()
        self.dialog.cash_btn.clicked.connect(self.total_cash_action)
        self.dialog.cashless_btn.clicked.connect(self.total_cashless_action)

    def total_cash_action(self):
        self.dialog = CashDialog(window)
        self.result = self.dialog.exec_()
        if self.result == QDialog.Accepted:
            try:
                self.buyer_cash = self.dialog.cashEdit.text()
            except:
                QMessageBox.critical(window, "Ошибка",
                                     "Некоректная сумма",
                                     buttons=QMessageBox.Ok,
                                     defaultButton=QMessageBox.Ok)
                self.total_cash_action()
            else:
                self.total_pre_cash_print_action()

    def total_cashless_action(self):
        self.dialog = CashlessDialog(window)
        self.result = self.dialog.exec_()
        if self.result == QDialog.Accepted:
            self.total_print_action(type='cash')

    def total_pre_cash_print_action(self):
        self.dialog = PrintCashDialog(window)
        self.odd_money = str(Decimal(
            self.check_price) + Decimal(self.buyer_cash))
        self.dialog.cashEdit.setText(self.odd_money)
        self.result = self.dialog.exec_()
        if self.result == QDialog.Accepted:
            self.total_print_action(type='cashless')

    def total_print_action(self, type):
        barcode_list = self.win.table_model.findItems("", flags=QtCore.Qt.MatchContains, column=0)
        count_list = self.win.table_model.findItems("", flags=QtCore.Qt.MatchContains, column=2)
        for barcode, count in zip(barcode_list, count_list):
            product = self.session.query(Product).filter(
                Product.barcode == barcode).first()
            product.on_stock -= Decimal(count.text())
            self.session.commit()
        if type=='cash':
            self.report.cash += Decimal(self.check_price)
        elif type=='cashless':
            self.report.cashless += Decimal(self.check_price)
        self.report.checks += 1
        self.session.commit()
        #print
        
        #clear
        self.win.table_model.clear()
        self.win.table_model.setHorizontalHeaderLabels(self.win.table_head_attr_list)
        self.check_price = 0
        self.win.barcodeEdit.setFocus()
        pass #here is print check script + data base (-)!
        # + self.check_price = 0 обнуляем чек
        # +self.win.table_model.clear() очищаем список товаров
        # +self.win.table_model.setHorizontalHeaderLabels(self.win.table_head_attr_list)
        # +report в бд + к сумме нал безнал + к чеку

    def auth_action(self):
        self.dialog = AuthDialog()
        self.result = self.dialog.exec_()
        if self.result == QDialog.Accepted:
            if self.dialog.passwordEdit.text() == '':
                QMessageBox.critical(self, "Ошибка",
                                     "Вы не ввели пароль",
                                     buttons=QMessageBox.Ok,
                                     defaultButton=QMessageBox.Ok)
                self.auth_action()
            else:
                if self.session.query(User).filter(
                    User.password == str(
                        self.dialog.passwordEdit.text())).first():
                    self.user_id = self.session.query(User.id).filter(
                        User.password == str(
                            self.dialog.passwordEdit.text())).first()
                    self.first_in_action()
                else:
                    QMessageBox.critical(self, "Ошибка",
                                         "Такого пароля не существует",
                                         buttons=QMessageBox.Ok,
                                         defaultButton=QMessageBox.Ok)
                    self.auth_action()
        else:
            QMessageBox.critical(self, "Ошибка",
                                 "Вы должны войти",
                                 buttons=QMessageBox.Ok,
                                 defaultButton=QMessageBox.Ok)
            self.auth_action()

    def on_clicked_settings_change(self):
        self.dialog = SettingsDialog(window)
        self.result = self.dialog.exec_()

    def closeEvent(self, event):
        reply = QMessageBox.critical(self, 'Error',
                        "Вы не можете завершить работу без закрытия смены",
                         QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.setWindowTitle("Project")
    window.resize(800, 640)
    window.show()
    sys.exit(app.exec_())


