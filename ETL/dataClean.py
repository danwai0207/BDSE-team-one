import pandas as pd
import numpy as np


#  df: dataframe
#  tag: column be search
#  L: list of condiction. if not in L then replace to be R
#  r: the number be replace
#  R: to replace the number which not fit condiction

def fill_null(df, tag, R):
    df.info()
    df[tag] = df[tag].fillna(R)


def replace_num(df, tag, r, R):
    df[tag] = df[tag].replace(r, R)


def check_condition(df, tag, L, R):
    df[tag] = np.where(~df[tag].isin(L), R, df[tag])


def drop_null(df, tag_list):
    return df.dropna(subset=tag_list)


def drop_dup(df, tag):
    return df.drop_duplicates(tag)
