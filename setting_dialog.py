# -*- coding: utf-8 -*-
#from PyQt4.QtGui import *
from decimal import *
#from PyQt4.QtCore import *
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QTextEdit, QMainWindow, QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QSettings
from dbmodel import *

class SettingsDialog(QDialog):
    defaults = {'addressDBServerEdit': 'localhost',
                'portDBServerEdit': '5432',
                'usingDBEdit': 'postgresql+psycopg2',
                'userNameEdit': 'postgres',
                'userPasswordEdit': '1111',
                'baseNameEdit': 'testbase',
                'cashboxNameEdit': ''
                }
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setWindowTitle('Settings')

        self.groupName = 'Settings'

        self.addressDBServerLabel = QLabel('server address')
        self.addressDBServerEdit = QLineEdit()
        self.portDBServerLabel = QLabel('server port')
        self.portDBServerEdit = QLineEdit()
        self.usingDBLabel = QLabel('using database protocol')
        self.usingDBEdit = QLineEdit()
        self.userNameLabel = QLabel('data base user name')
        self.userNameEdit = QLineEdit()
        self.userPasswordLabel = QLabel('data base user password')
        self.userPasswordEdit = QLineEdit()
        self.baseNameLabel = QLabel('database name')
        self.baseNameEdit = QLineEdit()
        self.cashboxNameLabel = QLabel('cashbox name')
        self.cashboxNameEdit = QLineEdit()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.addressDBServerLabel)
        self.mainLayout.addWidget(self.addressDBServerEdit)
        self.mainLayout.addWidget(self.portDBServerLabel)
        self.mainLayout.addWidget(self.portDBServerEdit)
        self.mainLayout.addWidget(self.usingDBLabel)
        self.mainLayout.addWidget(self.usingDBEdit)
        self.mainLayout.addWidget(self.userNameLabel)
        self.mainLayout.addWidget(self.userNameEdit)
        self.mainLayout.addWidget(self.userPasswordLabel)
        self.mainLayout.addWidget(self.userPasswordEdit)
        self.mainLayout.addWidget(self.baseNameLabel)
        self.mainLayout.addWidget(self.baseNameEdit)
        self.mainLayout.addWidget(self.cashboxNameLabel)
        self.mainLayout.addWidget(self.cashboxNameEdit)

        self.applyButton = QPushButton('Apply')
        self.cancelButton = QPushButton('Cancel')

        self.connect(self.applyButton, SIGNAL('clicked()'),
                     self.applyDialog)
        self.connect(self.cancelButton, SIGNAL('clicked()'),
                     self, SLOT('reject()'))

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(self.applyButton)
        buttonLayout.addWidget(self.cancelButton)

        self.mainLayout.addLayout(buttonLayout)
        self.setLayout(self.mainLayout)

        self.settings = QSettings('project')
        self.loadSettings()

    def applyDialog(self):
        """
        Метод для применения диалога.
        """
        self.saveSettings()
        self.accept()

    def saveSettings(self):
        """
        Метод сохранения настроек из вкладки диалога.
        """
        is_changed = False
        for name in self.defaults.keys():
            field = getattr(self, name)

            if type(field) is QLineEdit:
                value = field.text()
            elif type(field) is QCheckBox:
                value = field.isChecked()
            elif type(field) is QSpinBox:
                value = field.value()
            elif type(field) is QToolButton:
                value = self.borderColor_value.name()

            original_value = self.defaults[name]
            if original_value != value:
                is_changed = True
            self.settings.setValue(name, QVariant(value))
        return is_changed

    def loadSettings(self):
        """
        Метод загрузки настроек во вкладку диалога.
        """
        for name in self.defaults.keys():
            field = getattr(self, name)
            raw_value = self.settings.value(name, QVariant(self.defaults[name]))
            if type(field) is QLineEdit:
                value = raw_value.toString()
                field.setText(value)
            elif type(field) is QCheckBox:
                value = raw_value.toBool()
                field.setChecked(value)
            elif type(field) is QSpinBox:
                value, ok = raw_value.toInt()
                if ok:
                    field.setValue(value)
            elif type(field) is QToolButton:
                value = raw_value.toString()
                setattr(self, '%s_value' % name, QColor(value))

            # keep for compare when saving
            self.defaults[name] = value

