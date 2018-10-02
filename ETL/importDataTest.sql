show global variables like '%secure%';
-- http://www.datastudy.cc/article/9eab69923fe0b04245de1e0ca247e083
-- https://stackoverflow.com/questions/32737478/how-should-i-tackle-secure-file-priv-in-mysql
SET SESSION sql_mode= 'ANSI';


use tmall;

-- ----------------------------------<test_format1>-----------------------------------------------

-- import raw data to DB
create table test_format1(
	user_id int not null,
	merchant_id int not null
	-- prob float
    );

-- ALTER TABLE tmall.test_format1 DROP COLUMN prob;  --the prob column has no value in it, that will cause problem
-- TRUNCATE TABLE test_format1;  --clear contenr inside table

load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/tmall/data_format1/test_format1.csv'
into table test_format1
columns terminated by ','
optionally enclosed by '"'
escaped by '"'
lines terminated by '\n'
ignore 1 lines;


ALTER TABLE test_format1 ADD prob float;

SELECT * FROM tmall.test_format1 limit 100;



-- ----------------------------------<user_info_format1_2>------------------------------------------------- 
drop table user_info_format1_2;
create table user_info_format1_2(
	user_id int ,
	age_range int null , 
	gender char(4) null);

-- TRUNCATE TABLE test_format1;  --clear contenr inside table
load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/tmall/data_format1/user_info_format1-2.csv'
into table user_info_format1_2
columns terminated by ','
optionally enclosed by '"'
escaped by '"'
lines terminated by '\n'
ignore 1 lines;
-- set `gender` = null where `gender` = '';

SELECT * FROM tmall.user_info_format1_2 limit 100;




-- ----------------------------------<train_format1_2>-----------------------------------------------
drop table user_info_format1_2;
create table train_format1_2(
	user_id int ,
	merchant_id int null , 
	label char null);

-- TRUNCATE TABLE train_format1;  --clear contenr inside table
load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/tmall/data_format1/train_format1-2.csv'
into table train_format1_2
columns terminated by ','
optionally enclosed by '"'
escaped by '"'
lines terminated by '\n'
ignore 1 lines;

SELECT * FROM tmall.train_format1_2 limit 100;



-- ----------------------------------<user_log_format1_2>-----------------------------------------------
drop table user_log_format1_2;
create table user_log_format1_2(
	user_id int null,
	item_id int null,
    cat_id int null,
    seller_id int null,
    brand_id int null,  -- null number has problem(col:4430)
    time_stamp int null,
    action_type char null);

-- TRUNCATE TABLE user_log_format1;  --clear contenr inside table
load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/tmall/data_format1/user_log_format1-2.csv'
into table user_log_format1_2
columns terminated by ','
optionally enclosed by '"'
escaped by '"'
lines terminated by '\n'
ignore 1 lines;

SELECT * FROM tmall.user_log_format1_2 limit 100;






