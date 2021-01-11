import numpy as np
import pandas as pd

# 读取对数收益率数据
dataFrame = pd.read_csv('ShanDongYaoBo.csv')
lrr_data = dataFrame["lrr"]
lrr_data = lrr_data.values


# ES计算函数
def ES_daily(a, x):
    VaR = np.percentile(a, (1 - x) * 100)
    ES = a[a <= VaR].mean()
    return abs(ES)


# 输出ES值
print('95%置信水平下的ES为{:.2f}'.format( \
    ES_daily(lrr_data, 0.95)))
