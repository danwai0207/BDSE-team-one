# Project Framework
<img src="image/MVC Framework.png" width="100%">

## Data
**Task**
> 1. 找題目、找資料
>> * 檔案大小 > G
>> * 預期能做出完整結論的資料
>> * 目前提案:
>>> 1. 天貓
>>> 2. kaggle?
> 2. 網路爬蟲
>> * for 天貓，蒐集item_id對應的商品敘述(名稱、圖片、售價、...etc)
>> * for stock, stock_id, datetime, price, high, low, volume...
>> * for aigo, discuss after the seminar 8/31

**Tools** (maybe be used)
> 1. bs4
> 2. requests
> 3. openurl
> 4. urllib

## Extract-Transform-Load (ETL)
**Task**
> 1. parsing data type, string, int, float, date-time
> 2. filtering unreasonable scale, sorting by values 
> 3. join table, database design
> 4. save as *.db or *.csv

**Tools** (maybe be used)
> 1. shell scripts
> 2. Python
>> * pandas
>> * open
>> * str
>> * re
> 3. sqlite3
>> * insert into
>> * delete
>> * update
>> * order by
>> * group by
>> * having
>> * join

## Hadoop Destination Files System (HDFS)
**Task**
> 1. Building the hdfs
> 2. refer the framework that Mr. 松林 given 

**Tools** (maybe be used)
> 1. VMWare ? VirtualBox?
> 2. startup disk ?
> 3. based on Linux OS
>> * Docker
>> * Hadoop

## Parsing & Modeling
**Task**
> 1. Building some algorithm
>> * Logistic Regression (already)
>> * Recommender System (almost already)
>> * SVM (pending)
>> * KNN (pending)
> 2. MapReduce
>> * i have no idea
>> * due to 9/13 (2 weeks)

**Tools** (maybe be used)
> 1. Python
> 2. Java
> 3. Program infrastructure

## Database (SQLite)
**Task**
> 1. Bridge hdfs to server
>> * sqlite driver on hadoop
>> * sqlite database on server

**Tools** (maybe be used)
> 1. SQLite
> 2. Hadoop
> 3. Django (MVT) or Spring (MVC)

## Server
**Task**
> 1. Building a server host
> 2. integrating server code, static & template
>> * server code: manage urls, set urls' pattern, control the requests of view
>> * static: css, js, image, font, ...etc
>> * template: HTML

**Tools** (maybe be used)
> 1. Flask (MVC), Django (MVT) or Spring (MVC)
> 2. Using AJAX to parse the bridge between database and Javascript, for visualization

## WEB
**Task**
> 1. Static WEB
> 2. Dynamic WEB

**Tools** (maybe be used)
> 1. template
>> * HTML
>> * CSS
> 2. static
>> * JavaScripts
>> * jQuery
> 3. visualization (a part of static)
>> * Plotly.js
>> * D3.js 
