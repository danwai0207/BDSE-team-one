# -*-coding: utf-8 -*-
#! python3.6
import sys
import datetime as dt
import requests
import os
import pandas as pd
import sqlite3
import csv
import time


        
def date_trans(start1,end1):

    date_int={'year1':int(start1[:4]),'month1':int(start1[4:6]),'day1':int(start1[6:]),
              'year2':int(end1[:4]),'month2':int(end1[4:6]),'day2':int(end1[6:])}
    
    start_date = dt.datetime(date_int['year1'],date_int['month1'],date_int['day1'])
    end_date = dt.datetime(date_int['year2'],date_int['month2'],date_int['day2'])
    totaldays = (end_date - start_date).days + 1
    return start_date,totaldays


def get_content(start_date,totaldays):
    
    for daynumber in range(totaldays):
        date1=(start_date + dt.timedelta(days = daynumber)).date()

        five_sec_url='http://www.twse.com.tw/exchangeReport/MI_5MINS?response=csv&date=%s'%str(date1)
        r = requests.get(five_sec_url)
        con = r.text.split('\n')
        print(con)
        res = delIntro(con)
        print(res)
        insertDate(res,str(date1))

    
def delIntro(con):    # delete the introduction of content
    del con[0]
    del con[con.index('"說明:"\r'.encode('utf-8').decode('utf-8', 'ignore')):]  
    res = [[con[i].strip('=').strip() for i in range(len(con))][j][1:-2].replace(',','').split('\"\"') for j in range(len(con))]
    return res

    
def insertDate(res,date1):    # insert date to first column 
    res[0].insert(0,'日期')
    for i in range(len(res)-1):
        res[i+1].insert(0,date1)

        
def createTable():
    with sqlite3.connect('testDB') as DB:
        c=DB.cursor()
        createTable='''create table if not exists fiveSec (日期 date, 時間 time,累積委託買進筆數 int,  累積委託買進數量 int, 累積委託賣出筆數 int, 累積委託賣出數量 int, 累積成交筆數 int, 累積成交數量 int, 累積成交金額 int);'''
        c.execute(createTable)
        
        
def insertData(res):
    with sqlite3.connect('testDB') as DB:
        c=DB.cursor()
        c.executemany('insert into fiveSec values(?,?,?,?,?,?,?,?,?)',res[1:])
        
def selectData():
    with sqlite3.connect('testDB') as DB:
        df = pd.read_sql_query('select * from fiveSec',DB)
        print(df)

        
if __name__ =='__main__': 
    
    starttime = time.time()

    createTable()  

  #  start_date,totaldays=date_trans('20180810','20180810')
    start_date,totaldays=date_trans(sys.argv[1],sys.argv[2])
    
    get_content(start_date,totaldays)

    selectData()

    print('cost time:',time.time()-starttime)