# -*- coding: utf-8 -*-
def db_connect():
    user = 'postgres'
    password = '1111'
    server = '192.168.0.101'
    port = '5432'
    base_name = 'islandbeer1'
    type_name = 'postgresql+psycopg2'
    return type_name+'://'+user+':'+password+'@'+server+':'+port+'/'+base_name
