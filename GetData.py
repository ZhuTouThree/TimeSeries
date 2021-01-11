import tushare as ts
import pandas as pd
ts.set_token('shuruzijidetusharetoken')
pro = ts.pro_api()
df = pro.query('daily', ts_code='600529.SH', start_date='20190101', end_date='20201231')

df=pd.DataFrame(df)
#宁德时代
df.to_csv('ShanDongYaoBo.csv')