
-- delete row which datas are totally duplicate, then save it to new table
CREATE TABLE if not exists tmp_table 
as select distinct * from duplicate_del 

-- fill columns' null number as different conditcion
UPDATE tmp_table SET
  gender = IfNULL(gender,-1),
  name = IfNULL(name,'N')

-- change number  
  
-- drop original table
drop table duplicate_del




