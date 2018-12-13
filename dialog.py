# -*- coding: utf-8 -*-
#from PyQt4.QtGui import *
#from PyQt4.QtCore import *
#from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QMessageBox
from dbmodel import *

class FirstInDialog(QDialog):    #первое внесение без кнопки отмена
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle('Внесение')

        self.inputLabel = QLabel('Сумма для внесения')
        self.inputEdit = QLineEdit(self)

        self.btnOK = QPushButton("&OK")
        self.btnOK.clicked.connect(self.accept)
        self.mainBox = QVBoxLayout()
        self.mainBox.addWidget(self.inputLabel)
        self.mainBox.addWidget(self.inputEdit)
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.btnOK)
        self.mainBox.addLayout(self.hbox)

        self.setLayout(self.mainBox)

    def closeEvent(self, event):
        reply = QMessageBox.critical(self, 'Error',
                    "Вы не можете начать работу без внесения", QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.ignore()

class InDialog(QDialog):    #внесение
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle('Внесение')

        self.inputLabel = QLabel('Сумма для внесения')
        self.inputEdit = QLineEdit(self)

        self.btnOK = QPushButton("&OK")
        self.btnCancel = QPushButton("&Cancel")
        self.btnOK.clicked.connect(self.accept)
        self.btnCancel.clicked.connect(self.reject)
        self.mainBox = QVBoxLayout()
        self.mainBox.addWidget(self.inputLabel)
        self.mainBox.addWidget(self.inputEdit)
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.btnOK)
        self.hbox.addWidget(self.btnCancel)
        self.mainBox.addLayout(self.hbox)

        self.setLayout(self.mainBox)

class OutDialog(QDialog):#изъятие
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle('Изъятие')

        self.outputLabel = QLabel('Сумма для изъятия')
        self.outputEdit = QLineEdit(self)

        self.btnOK = QPushButton("&OK")
        self.btnCancel = QPushButton("&Cancel")
        self.btnOK.clicked.connect(self.accept)
        self.btnCancel.clicked.connect(self.reject)
        self.mainBox = QVBoxLayout()
        self.mainBox.addWidget(self.outputLabel)
        self.mainBox.addWidget(self.outputEdit)
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.btnOK)
        self.hbox.addWidget(self.btnCancel)
        self.mainBox.addLayout(self.hbox)

        self.setLayout(self.mainBox)

class ReportDialog(QDialog):#отчет
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle('Отчет')

        self.reportLabel = QLabel('Совершить отчет по кассе?')

        self.btnOK = QPushButton("&OK")
        self.btnCancel = QPushButton("&Cancel")
        self.btnOK.clicked.connect(self.accept)
        self.btnCancel.clicked.connect(self.reject)

        self.mainBox = QVBoxLayout()
        self.mainBox.addWidget(self.reportLabel)
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.btnOK)
        self.hbox.addWidget(self.btnCancel)
        self.mainBox.addLayout(self.hbox)

        self.setLayout(self.mainBox)

class CloseDialog(QDialog):#Закрытие
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle('Закрытие кассы')

        self.closeLabel = QLabel('Закрыть кассу?')

        self.btnOK = QPushButton("&OK")
        self.btnCancel = QPushButton("&Cancel")
        self.btnOK.clicked.connect(self.accept)
        self.btnCancel.clicked.connect(self.reject)

        self.mainBox = QVBoxLayout()
        self.mainBox.addWidget(self.closeLabel)
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.btnOK)
        self.hbox.addWidget(self.btnCancel)
        self.mainBox.addLayout(self.hbox)

        self.setLayout(self.mainBox)

class CancelDialog(QDialog):#отмена
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle('Отмена чека')

        self.cancelLabel = QLabel('Отменить чек?')

        self.btnOK = QPushButton("&OK")
        self.btnCancel = QPushButton("&Cancel")
        self.btnOK.clicked.connect(self.accept)
        self.btnCancel.clicked.connect(self.reject)

        self.mainBox = QVBoxLayout()
        self.mainBox.addWidget(self.cancelLabel)
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.btnOK)
        self.hbox.addWidget(self.btnCancel)
        self.mainBox.addLayout(self.hbox)

        self.setLayout(self.mainBox)

class DeleteDialog(QDialog):#отмена
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle('Отмена чека')

        self.deleteLabel = QLabel('Удалить товар?')
        self.deleteEdit = QLineEdit()
        self.deleteEdit.setReadOnly(True)

        self.btnOK = QPushButton("&OK")
        self.btnCancel = QPushButton("&Cancel")
        self.btnOK.clicked.connect(self.accept)
        self.btnCancel.clicked.connect(self.reject)

        self.mainBox = QVBoxLayout()
        self.mainBox.addWidget(self.deleteLabel)
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.btnOK)
        self.hbox.addWidget(self.btnCancel)
        self.mainBox.addLayout(self.hbox)

        self.setLayout(self.mainBox)

class MultiIncrementDialog(QDialog):    #инкремент продуктов
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle('Увеличение кол-ва')

        self.incrementLabel = QLabel('Введите количество товаров')
        self.incrementEdit = QLineEdit(self)

        self.btnOK = QPushButton("&OK")
        self.btnCancel = QPushButton("&Cancel")
        self.btnOK.clicked.connect(self.accept)
        self.btnCancel.clicked.connect(self.reject)
        self.mainBox = QVBoxLayout()
        self.mainBox.addWidget(self.incrementLabel)
        self.mainBox.addWidget(self.incrementEdit)
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.btnOK)
        self.hbox.addWidget(self.btnCancel)
        self.mainBox.addLayout(self.hbox)

        self.setLayout(self.mainBox)

class TotalDialog(QDialog):#посчитать итог
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle('Итог')

        self.cashLabel = QLabel('Выберите способ оплаты?')
        self.cash_btn = QPushButton("Наличный")
        self.cashless_btn = QPushButton("Безналичный")

        self.btnCancel = QPushButton("&Cancel")
        self.btnCancel.clicked.connect(self.reject)

        self.mainBox = QVBoxLayout()
        self.mainBox.addWidget(self.cashLabel)
        self.cash_type = QHBoxLayout()
        self.cash_type.addWidget(self.cash_btn)
        self.cash_type.addWidget(self.cashless_btn)
        self.mainBox.addLayout(self.cash_type)
        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.btnCancel)
        self.mainBox.addLayout(self.hbox)

        self.setLayout(self.mainBox)

class CashDialog(QDialog):#диалог нала
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle('Наличный расчет')

        self.cashLabel = QLabel('Введите сумму')
        self.cashEdit = QLineEdit()

        self.btnOK = QPushButton("&OK")
        self.btnOK.clicked.connect(self.accept)
        self.btnCancel = QPushButton("&Cancel")
        self.btnCancel.clicked.connect(self.reject)

        self.mainBox = QVBoxLayout()
        self.mainBox.addWidget(self.cashLabel)
        self.mainBox.addWidget(self.cashEdit)
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.btnOK)
        self.hbox.addWidget(self.btnCancel)
        self.mainBox.addLayout(self.hbox)

        self.setLayout(self.mainBox)

class PrintCashDialog(QDialog):#печать чека
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle('Наличный расчет')

        self.cashLabel = QLabel('Выдайте сдачу в размере:')
        self.cashEdit = QLineEdit()
        self.cashEdit.setReadOnly(True)

        self.btnOK = QPushButton("&Печать чека")
        #self.btnCancel = QPushButton("&Отмена")
        self.btnOK.clicked.connect(self.accept)
        #self.btnCancel.clicked.connect(self.reject)

        self.mainBox = QVBoxLayout()
        self.mainBox.addWidget(self.cashLabel)
        self.mainBox.addWidget(self.cashEdit)
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.btnOK)
        #self.hbox.addWidget(self.btnCancel)
        self.mainBox.addLayout(self.hbox)

        self.setLayout(self.mainBox)

class CashlessDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle('Безналичный расчет')

        self.cashlessLabel = QLabel('Оплачено?')

        self.btnOK = QPushButton("&Печать чека")
        self.btnCancel = QPushButton("&Отмена")
        self.btnOK.clicked.connect(self.accept)
        self.btnCancel.clicked.connect(self.reject)

        self.mainBox = QVBoxLayout()
        self.mainBox.addWidget(self.cashlessLabel)
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.btnOK)
        self.hbox.addWidget(self.btnCancel)
        self.mainBox.addLayout(self.hbox)

        self.setLayout(self.mainBox)

class AuthDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle('Авторизация')

        self.passwordLabel = QLabel('Введите пароль?')
        self.passwordEdit = QLineEdit()
        self.passwordEdit.setEchoMode(QLineEdit.Password)

        self.btnOK = QPushButton("&OK")
        self.btnCancel = QPushButton("&Отмена")
        self.btnOK.clicked.connect(self.accept)
        self.btnCancel.clicked.connect(self.reject)

        self.mainBox = QVBoxLayout()
        self.mainBox.addWidget(self.passwordLabel)
        self.mainBox.addWidget(self.passwordEdit)
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.btnOK)
        self.hbox.addWidget(self.btnCancel)
        self.mainBox.addLayout(self.hbox)

        self.setLayout(self.mainBox)

    def closeEvent(self, event):
        reply = QMessageBox.critical(self, 'Error',
                                         "Вы не можете начать работу без авторизации", QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.ignore()