import pymysql
from sqlalchemy import create_engine
import gc


def df_to_mysql(df, df_name, user, pwd, ip, port, db, charset, if_exists = 'replace', index = False, chunksize = 50000):
    s = time.time()
    engine = create_engine("mysql+pymysql://%s:%s@%s:%s/%s?charset=%s"%(user, pwd, ip, port, db, charset)) 

    df.to_sql(name =  df_name+'_2', con = engine,if_exists = 'replace', index = False, chunksize = 50000)
    s3 = time.time()
    print('insert "%s" to mysql cost time:'%( df_name+'_2'), time.time()-s)

    del [[df]]
    gc.collect()