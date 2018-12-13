# -*- coding: utf-8 -*-
#from PyQt4.QtGui import *
#from PyQt4.QtCore import *
#from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from dbmodel import *

class MainWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        #QToolTip.setFont(QFont('SansSerif', 15))

        #self.setToolTip('Эта кнопка Внесения в кассу')
        #self.setToolTip('Эта кнопка Изъятия из кассы')
        #self.setToolTip('Эта кнопка Отчета по кассе')
        #self.setToolTip('Эта кнопка Закрытия кассы')
        #self.setToolTip('Эта кнопка Отмены чека')
        #self.setToolTip('Эта кнопка Удаления товара')

        self.in_btn = QPushButton('Внесение (in)', self)
        self.out_btn = QPushButton('Изъятие (out)', self)
        self.report_btn = QPushButton('Отчет (report)', self)
        self.close_btn = QPushButton('Закрытие (Close)', self)
        self.cancel_btn = QPushButton('Отмена чека (C)', self)
        self.delete_btn = QPushButton('Удаление товара (D)', self)
        self.increment_btn = QPushButton('Количество (K)', self)
        self.total_btn = QPushButton('Посчитать итог', self)

        self.barcodeLabel = QLabel('Штрихкод')
        self.barcodeEdit = QLineEdit()
        self.totalLabel = QLabel('Итог')
        self.totalEdit = QLineEdit()
        self.totalEdit.setMaxLength(50)#может дело и не в этом
        self.totalEdit.setReadOnly(True)
        self.table_head_attr_list = ['Штрихкод',
                                     'Товар',
                                     'кол-во',
                                     'price',
                                     ]
        self.table_model = QStandardItemModel()
        self.table_model.setHorizontalHeaderLabels(self.table_head_attr_list)
        self.table = QTableView()

        self.table.setModel(self.table_model)
        self.table.resizeColumnsToContents()
        self.table.setSortingEnabled(True)
        self.table.setCornerButtonEnabled(False)
        #self.table.setColumnWidth(0, 400)
        #self.table.setColumnWidth(1, 75)
        #self.table.setColumnWidth(2, 75)

        self.v_btn_box = QVBoxLayout()
        self.v_btn_box.addWidget(self.in_btn)
        self.v_btn_box.addWidget(self.out_btn)
        self.v_btn_box.addWidget(self.report_btn)
        self.v_btn_box.addWidget(self.close_btn)
        self.v_btn_box.addStretch(1)
        self.v_btn_box.addWidget(self.increment_btn)
        self.v_btn_box.addWidget(self.cancel_btn)
        self.v_btn_box.addWidget(self.delete_btn)

        self.h_total_box = QHBoxLayout()
        self.h_total_box.addStretch(1)
        self.h_total_box.addWidget(self.totalLabel)
        self.h_total_box.addWidget(self.totalEdit)
        self.h_total_box.addWidget(self.total_btn)

        self.h_barcode_box = QHBoxLayout()
        self.h_barcode_box.addStretch(1)
        self.h_barcode_box.addWidget(self.barcodeLabel)
        self.h_barcode_box.addWidget(self.barcodeEdit)

        self.v_main_content_box = QVBoxLayout()
        self.v_main_content_box.addLayout(self.h_barcode_box)
        self.v_main_content_box.addWidget(self.table)
        self.v_main_content_box.addLayout(self.h_total_box)

        self.mainBox = QHBoxLayout()
        self.mainBox.addLayout(self.v_btn_box)
        self.mainBox.addLayout(self.v_main_content_box)

        self.setLayout(self.mainBox)

        self.in_btn.setToolTip('Эта кнопка <b>Внесения</b> в кассу')
        self.in_btn.resize(self.in_btn.sizeHint())
        self.out_btn.setToolTip('Эта кнопка <b>Изъятия</b> из кассы')
        self.out_btn.resize(self.out_btn.sizeHint())
        self.report_btn.setToolTip('Эта кнопка <b>Отчета</b> по кассе')
        self.report_btn.resize(self.report_btn.sizeHint())
        self.close_btn.setToolTip('Эта кнопка <b>Закрытия</b> кассы')
        self.close_btn.resize(self.close_btn.sizeHint())
        self.cancel_btn.setToolTip('Эта кнопка <b>Отмены</b> чека')
        self.cancel_btn.resize(self.cancel_btn.sizeHint())
        self.delete_btn.resize(self.delete_btn.sizeHint())

