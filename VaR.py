from scipy.stats import norm
import pandas as pd
#读取对数收益率数据
dataFrame = pd.read_csv('ShanDongYaoBo.csv')
lrr_data = dataFrame["lrr"]
lrr_data = lrr_data.values
#计算均值 方差以及标准差
u = lrr_data.mean()
var=lrr_data.var()
std=lrr_data.std()
#输出VaR度量值
Z_05=-norm.ppf(0.95)
print(Z_05*std-u)

