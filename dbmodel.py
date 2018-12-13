# -*- coding: utf-8 -*-
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DECIMAL, Enum, TIMESTAMP
from sqlalchemy.orm import relationship
from dbengine import db_connect

Base = declarative_base()

class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True)
    subgroup = relationship( 'SubGroup', backref='group ')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "%s" % ( self.name)

class SubGroup(Base):
    __tablename__ = 'subgroup'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True)
    group_id = Column(Integer, ForeignKey('group.id'))
    product = relationship('Product', backref='subgroup')

    def __init__(self, name, group_id):
        self.name = name
        self.group_id = group_id

    def __repr__(self):
        return "%s" % (self.name)

class Product(Base) :
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    subgroup_id = Column(Integer, ForeignKey('subgroup.id'))
    name = Column(String(250), unique=True)
    barcode = Column (String(250), unique=True)
    purchase_price =  Column (DECIMAL, nullable=True)
    delivery_number = Column (DECIMAL, nullable=True)
    on_stock = Column (DECIMAL, nullable=True)
    Write_off = Column (DECIMAL, nullable=True)
    delivery_time = Column (TIMESTAMP, nullable=True)
    write_off_time = Column (TIMESTAMP, nullable=True)
    type = Column(Enum('sht', 'kg', 'litr', 'upak', name='product_type'))

    def __init__(self, subgroup_id, name, barcode, type):
        self.subgroup_id = subgroup_id
        self.name = name
        self.barcode = barcode
        self.type = type

    def __repr__(self):
        return "Barcode: %s  %s |%s" % (self.barcode, self.name, self.subgroup_id)

class CashBox(Base):
    __tablename__ = 'cashbox'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    report = relationship('Report', backref='cashbox')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Касса: %s" % (self.name)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    password = Column(String(250))
    report = relationship('Report', backref='user')

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return "%s" % (self.name)

class Report(Base):
    __tablename__ = 'report'
    id = Column(Integer, primary_key=True)
    cashbox_id = Column(Integer, ForeignKey('cashbox.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    cash = Column (DECIMAL)
    cashless = Column (DECIMAL)
    checks = Column (Integer)
    amendment = Column (DECIMAL)
    withdrawal = Column (DECIMAL)
    open_time = Column(TIMESTAMP)
    close_time = Column (TIMESTAMP)

    def __init__(self, cashbox_id, user_id):
        self.cashbox_id = cashbox_id
        self.user_id = user_id
        self.cash = 0
        self.cashless = 0
        self.checks = 0
        self.amendment = 0
        self.withdrawal = 0
        self.open_time = datetime.datetime.now()

class GrossItog(Base):
    __tablename__ = 'gross itog'
    id = Column(Integer, primary_key=True)
    cash = Column(DECIMAL)
    cashless = Column(DECIMAL)
    null_date = Column (TIMESTAMP)

    def __init__(self):
        self.cash = 0
        self.cashless = 0
        self.null_date = datetime.datetime.now()

Group.__table__
Group.__mapper__
SubGroup.__table__
SubGroup.__mapper__
Product.__table__
Product.__mapper__
CashBox.__table__
CashBox.__mapper__
User.__table__
User.__mapper__
Report.__table__
Report.__mapper__
GrossItog.__tablename__
GrossItog.__mapper__

engine = create_engine(db_connect(), echo=True)
#engine = create_engine('postgresql+psycopg2://project_user:1111@localhost:5432/project_data_base', echo=True)
Base.metadata.create_all(engine)
'''
def main():
    #engine = create_engine('postgresql+psycopg2://project_user:1111@localhost:5432/project_data_base', echo=True)
    engine = create_engine(db_connect(), echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    group1 = Group('Группа 1')
    group2 = Group('Группа 2')
    group3 = Group('Группа 3')
    group4 = Group('Группа 4')
    group5 = Group('Группа 5')
    group6 = Group('Группа 6')
    group7 = Group('Группа 7')
    subgroup1group1 = SubGroup('SubGroup 1 Group 1', 1)
    subgroup2group1 = SubGroup('SubGroup 2 Group 1', 1)
    subgroup3group1 = SubGroup('SubGroup 3 Group 1', 1)
    subgroup1group2 = SubGroup('SubGroup 1 Group 2', 2)
    subgroup2group2 = SubGroup('SubGroup 2 Group 2', 2)
    subgroup3group2 = SubGroup('SubGroup 3 Group 2', 2)
    subgroup1group3 = SubGroup('SubGroup 1 Group 3', 3)
    subgroup2group3 = SubGroup('SubGroup 2 Group 3', 3)
    subgroup3group3 = SubGroup('SubGroup 3 Group 3', 3)
    subgroup1group4 = SubGroup('SubGroup 1 Group 4', 4)
    subgroup2group4 = SubGroup('SubGroup 2 Group 4', 4)
    subgroup3group4 = SubGroup('SubGroup 3 Group 4', 4)
    subgroup1group5 = SubGroup('SubGroup 1 Group 5', 5)
    subgroup2group5 = SubGroup('SubGroup 2 Group 5', 5)
    subgroup3group5 = SubGroup('SubGroup 3 Group 5', 5)
    subgroup1group6 = SubGroup('SubGroup 1 Group 6', 6)
    subgroup2group6 = SubGroup('SubGroup 2 Group 6', 6)
    subgroup3group6 = SubGroup('SubGroup 3 Group 6', 6)
    subgroup1group7 = SubGroup('SubGroup 1 Group 7', 7)
    subgroup2group7 = SubGroup('SubGroup 2 Group 7', 7)
    subgroup3group7 = SubGroup('SubGroup 3 Group 7', 7)
    subgroup4group7 = SubGroup('SubGroup 4 Group 7', 7)
    subgroup5group7 = SubGroup('SubGroup 5 Group 7', 7)
    subgroup6group7 = SubGroup('SubGroup 6 Group 7', 7)
    session.add(group1)
    session.add(group2)
    session.add(group3)
    session.add(group4)
    session.add(group5)
    session.add(group6)
    session.add(group7)
    session.add(subgroup1group1)
    session.add(subgroup2group1)
    session.add(subgroup3group1)
    session.add(subgroup1group2)
    session.add(subgroup2group2)
    session.add(subgroup3group2)
    session.add(subgroup1group3)
    session.add(subgroup2group3)
    session.add(subgroup3group3)
    session.add(subgroup1group4)
    session.add(subgroup2group4)
    session.add(subgroup3group4)
    session.add(subgroup1group5)
    session.add(subgroup2group5)
    session.add(subgroup3group5)
    session.add(subgroup1group6)
    session.add(subgroup2group6)
    session.add(subgroup3group6)
    session.add(subgroup1group7)
    session.add(subgroup2group7)
    session.add(subgroup3group7)
    session.add(subgroup4group7)
    session.add(subgroup5group7)
    session.add(subgroup6group7)
    session.commit()


'''
