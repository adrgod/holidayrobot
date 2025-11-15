
#all functions to work on the data will be here
import functools
import time
from support.performance import timer

@timer
def fitler_first_year(df):
    return df[df['Statistic Label'].str.contains('First Year')]

@timer
def rename_header(df):
    df.columns = df.columns.str.lower()
    return df