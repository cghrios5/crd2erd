import glob
import csv
import os

import numpy as np
import pandas as pd
import datetime

csvs = glob.glob('path/to/csv/file/*.csv')
count = 0

f = open('./csv2erd_{}.csv','w')
writer = csv.writer(f)
    

header = ["dbms","table_schema","table_name","column_name","ordinal_position","data_type"]
writer.writerow(header)

for csv in csvs:
    print('---------------------------')
    print(os.path.basename(csv))
    csv_basename =(os.path.basename(csv)).split('.')[0]
    df = pd.read_csv(csv)
    cols = list(df)
    print(f'cols: {list(df)}')
    for col in cols:
      dtype = str(df[col].dtype)
      row = ["postgres","public",csv_basename,col,count,dtype]
      print (row)
      writer.writerow(row)
      count += 1
f.close()


# then go to url 
# https://cacoo.com/
# 挿入データベーススキーマ
