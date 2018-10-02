import pandas as pd
import numpy as np
import time
from dataClean import *
import to_mysql
import gc

gc.collect()

s = time.time()
dfName = ['user_info_format1', 'train_format1', 'user_log_format1']

df1 = pd.read_csv('../data_format1/%s.csv'%dfName[0], sep=',')
df2 = pd.read_csv('../data_format1/%s.csv'%dfName[1], sep=',')
df3 = pd.read_csv('../data_format1/%s.csv'%dfName[2], sep=',')

s0 = time.time()
print('read data cost time:', s0-s)

# ---------------------------------------------------------------------------------
# 'user_info_format1'
df1=drop_null(df1, ['user_id'])    # drop should be first, that can cut calculate short
df1=drop_dup(df1, ['user_id'])
fill_null(df1, 'gender', 2)
fill_null(df1, 'age_range', 0)
replace_num(df1, "age_range", 8, 7)
check_condition(df1, 'gender', [0, 1, 2], 2)

s1=time.time()
print('clean %s table cost time:'%dfName[0],s1-s0)

# export data: 'user_info_format1-2'
df1.to_csv(r'../data_format1/%s-2.csv'%dfName[0],sep=',', index=False, mode='a')
s2=time.time()
print('save %s table to csv as "%s-2.csv" cost time:'%(dfName[0], dfName[0]), s2-s1)
df_to_mysql(df1, dfName[0], 'user01', 'user01', '192.168.31.73', '3306', 'tmall', 'utf8')

# -----------------------------------------------------------------------------------------
# 'train_format1'
df2 = drop_null(df2, ['user_id', 'merchant_id', 'label'])
df2 = drop_dup(df2, ['user_id', 'merchant_id', 'label'])
check_condition(df2, 'label', [0, 1], np.nan)    # if label's content is not 1 or 0 , than put it NaN
df2 = drop_null(df2, ['label'])    # drop row that we put NaN

s3=time.time()
print('clean %s table cost time:'%dfName[1], s3-s2)

# export data: 'train_format1-2'
df2.to_csv(r'%s-2.csv'%dfName[1], sep=',', index=False, mode='a')
s4 = time.time()
print('save %s table to csv as "%s-2.csv" cost time:'%(dfName[1], dfName[1]), s4-s3)
df_to_mysql(df2, dfName[1], 'user01', 'user01', '192.168.31.73', '3306', 'tmall', 'utf8')

# -----------------------------------------------------------------------------------------
# 'user_log_format1'
df3 = drop_dull(df3, ['user_id', 'item_id'])
d32 = drop_dup(df3, ['user_id', 'item_id', 'cat_id', 'seller_id', 'brand_id', 'time_stamp', 'action_type'])
replace_num(df3, "cat_id", np.nan, -1)
replace_num(df3, "seller_id", np.nan, -1)
replace_num(df3, "brand_id", np.nan, -1)
replace_num(df3, "time_stamp", np.nan, -1)
replace_num(df3, "action_type", np.nan, -1)

s5=time.time()
print('clean %s table cost time:'%dfName[2],s5-s4)

# export data; 'user_log_format1-2'
df3.to_csv(r'%s-2.csv'%dfName[2], sep=',', index=False, mode='a')
s6 = time.time()
print('save %s table to csv as "%s-2.csv" cost time:'%(dfName[2], dfName[2]), s6-s5)
df_to_mysql(df3, dfName[2], 'user01', 'user01', '192.168.31.73', '3306', 'tmall', 'utf8')